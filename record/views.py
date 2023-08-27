from typing import Any, Dict
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import Q
from . import models
from . import forms
from django.utils import timezone
from django.core.paginator import Paginator
from . import pageRequest
from django.core import serializers
from django.contrib.auth.mixins import LoginRequiredMixin


class MainView(TemplateView):
    template_name = "record/main.html"

    # 파라미터 보내기
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            
            # 로그인한 유저네임
            loginedUsername = self.request.user.username

            # context["name"] = loginedUsername
            # 해당 유저 인스턴스
            user = models.User.objects.get(username__contains=loginedUsername)

            # 해당 유저의 애완동물
            pets = user.pet_set.all() 
            context["pets"] = pets
            return context
        
# 애완동물 추가 페이지
class AddPetView(LoginRequiredMixin, CreateView):
    model = models.Pet # 연결할 모델 클래스

    # 커스텀 폼 클래스
    form_class = forms.AddPetForm

    # 요청에 성공했을 시 이동할 URL
    success_url = reverse_lazy("record:main")


    # 폼을 전달받았을 때 호출되는 함수 
    def form_valid(self, form):

        # 유저 아이디 지정
        # 로그인한 유저네임
        loginedUsername = self.request.user.username

        user = models.User.objects.get(username__contains=loginedUsername)

        form.instance.userID = user

        return super().form_valid(form)
    

# 기록 리스트
class RecordListView(LoginRequiredMixin, ListView):
    model = models.Records

    # 쿼리셋 지정
    def get_queryset(self) :
        petID = self.kwargs["petID"]

        ordering = self.request.GET.get("ordering")
        filtering= self.request.GET.get("filter")

        if filtering is not None:
            if filtering == "feed":
                q = Q(petId_id=petID, feeding__isnull=False)
            elif filtering == "weight":
                q = Q(petId_id=petID, weight__isnull=False)
            elif filtering == "molting":
                q = Q(petId_id=petID, molting=True)
            else :
                q = Q(petId_id=petID)
        else :
            q = Q(petId_id=petID)

        if ordering is not None:
            if ordering == "asc":
                queryset = models.Records.objects.filter(q).order_by("id")    
            else:
                queryset = models.Records.objects.filter(q).order_by("-id")
        else :
            queryset = models.Records.objects.filter(q).order_by("-id")

        return queryset

    # 추가로 전달할 파라미터 지정
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        #  URL로 전달된 매개변수를 가져옴
        petID = self.kwargs['petID']

        # ID를 사용하여 인스턴스를 가져옴
        pet = models.Pet.objects.get(id=petID)
        # 추가로 전달할 파라미터 지정
        context["pet"] = pet

        # 정렬 방식
        ordering = self.request.GET.get("ordering")
        context["ordering"] = ordering

        # 필터
        filtering = self.request.GET.get("filter")
        context["filter"] = filtering


        # 페이징
        # 페이지 번호
        page = self.request.GET.get("page")
        
        # 페이징 객체
        queryset = self.get_queryset()
        paginator = Paginator(queryset, 10)
        context["paginator"] = paginator

        # 페이지 번호 예외처리
        if page == None:
            page = 1
        elif int(page) > paginator.num_pages:
            page = paginator.num_pages
        
        # 페이징 처리된 객체들
        pageObj = paginator.page(page)
        context["pageObj"] = pageObj

        # 표시할 페이지 레인지
        startPage = ((int(page)-1) // 5) * 5 + 1
        endPage = (((int(page)-1) // 5) + 1) * 5
        if endPage > paginator.num_pages:
            endPage = paginator.num_pages
        pageRange = range(startPage, endPage+1) 
        context["pageRange"] = pageRange
        context["startPage"] = startPage
        context["beforePage"] = startPage-1
        context["endPage"] = endPage
        context["nextPage"] = endPage+1

        return context


class UpdatePetView(LoginRequiredMixin, UpdateView):
    model = models.Pet # 연결할 모델 클래스

    # 커스텀 폼 클래스
    form_class = forms.AddPetForm

    template_name_suffix = "_update_form"

    def get_success_url(self):
        # 요청 성공 후 이동할 petID와 페이지, 필터, 정렬 정보를 포함한 URL을 반환

        page_request = pageRequest.PageRequest()

        filtering = self.request.GET.get("filter")
        ordering = self.request.GET.get("ordering")
        page = self.request.GET.get("page")

        parameter = page_request.getParameter(filtering, ordering, page)

        success_url = reverse_lazy('record:recordList', kwargs={"petID": self.object.pk})
        success_url += parameter

        return success_url
    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        page_request = pageRequest.PageRequest()

        filtering = self.request.GET.get("filter")
        ordering = self.request.GET.get("ordering")
        page = self.request.GET.get("page")

        context = page_request.getContext(context, filtering, ordering, page)

        return context


class DeletePetView(LoginRequiredMixin, DeleteView):
    model = models.Pet

    template_name_suffix = "_delete"

    # 성공시 이동할 페이지
    def get_success_url(self) :

        success_url = reverse_lazy('record:main')
       
        return success_url
    


class RecordView(LoginRequiredMixin, CreateView):
    model = models.Records # 연결할 모델 클래스

    # 커스텀 폼 클래스
    form_class = forms.RecordForm


    # 폼을 전달받았을 때 호출되는 함수 
    def form_valid(self, form):

        # 해당 에완동물 지정
        # 기록할 애완동물 id 지정
        petID = self.kwargs["pk"]

        pet = models.Pet.objects.get(id=petID)

        form.instance.petId = pet

        # 날짜를 오늘 날짜로 지정
        today = timezone.now()
        form.instance.date = today

        return super().form_valid(form)
    
    def get_success_url(self):
        # 요청 성공 후 이동할 petID와 페이지 반환

        success_url = reverse_lazy('record:recordList', kwargs={"petID": self.kwargs["pk"]})
   
        return success_url


class RecordDetailView(LoginRequiredMixin, DetailView):
    model = models.Records

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_request = pageRequest.PageRequest()

        filtering = self.request.GET.get("filter")
        ordering = self.request.GET.get("ordering")
        page = self.request.GET.get("page")

        context = page_request.getContext(context, filtering, ordering, page)

        return context

class DeleteRecordView(LoginRequiredMixin, DeleteView):

    model = models.Records

    template_name_suffix = "_delete"

     # 성공시 이동할 페이지
    def get_success_url(self) :

        page_request = pageRequest.PageRequest()

        filtering = self.request.GET.get("filter")
        ordering = self.request.GET.get("ordering")
        page = self.request.GET.get("page")

        parameter = page_request.getParameter(filtering, ordering, page)

        success_url = reverse_lazy('record:recordList',  kwargs={"petID": self.object.petId_id})
        success_url += parameter
       
        return success_url
    

class UpdateRecordView(LoginRequiredMixin, UpdateView):
    model = models.Records # 연결할 모델 클래스

    # 커스텀 폼 클래스
    form_class = forms.RecordForm

    template_name_suffix = "_update_form"

    def get_success_url(self):
        # 요청 성공 후 이동할 petID와 페이지, 필터, 정렬 정보를 포함한 URL을 반환

        page_request = pageRequest.PageRequest()

        filtering = self.request.GET.get("filter")
        ordering = self.request.GET.get("ordering")
        page = self.request.GET.get("page")

        parameter = page_request.getParameter(filtering, ordering, page)

        success_url = reverse_lazy('record:recordList', kwargs={"petID": self.object.petId_id})
        success_url += parameter

        return success_url


class GraphView(LoginRequiredMixin, TemplateView):
    template_name = "record/graph.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        petID = self.kwargs["pk"]

        context["pk"] = petID

        value = self.request.GET.get("value")
        if value == None:
            value = "Weight"

        context["value"] = value


        # 그래프에 표시할 데이터]

        if value == "feeding":
            q = Q(petId_id=self.kwargs["pk"], feededWeight__isnull=False)
        else:
            q = Q(petId_id=self.kwargs["pk"], weight__isnull=False)

        data = models.Records.objects.filter(q).order_by("date")
        data_json = serializers.serialize("json", data)

        context["data"] = data_json

        print(data_json)

        return context
    
    




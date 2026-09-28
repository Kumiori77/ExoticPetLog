

from django.utils import timezone

from django import forms
from . import models

# 애완 동물 추가 폼
class AddPetForm(forms.ModelForm):
    class Meta:
        model = models.Pet

        fields = ["name", "species", "isBeingReared"]

        labels = {
            "name":"이름 ",
            "species":"종류 ",
            "isBeingReared":"사육중"
        }

# 기록 폼
class RecordForm(forms.ModelForm):
    class Meta:
        model = models.Records

        fields = ["weight", "feeding", "feededWeight", "molting", "image"]

        labels = {
            "weight":"무게(g)",
            "feeding":"피딩 (먹이 종류)",
            "feededWeight":"피딩 무게(g)",
            "molting":"탈피 여부",
            "image":"사진"
        }
        label_suffix = ''  # 콜론(:) 제외

# 대시보드 폼
class DashboardForm(forms.ModelForm):
    date = forms.DateField(
        initial=timezone.localdate,
        widget=forms.DateInput(
            format="%Y-%m-%d",
            attrs={"type": "date"}
        )
    )


    class Meta:
        model = models.Dashboard

        fields = ["date", "state", "note"]

        labels = {
            "date":"날짜",
            "state":"상태",
            "note":"비고"
        }

        label_suffix = ''  # 콜론(:) 제외

        widgets = {
            'date': forms.DateInput(
                format='%Y-%m-%d',
                attrs={'type': 'date'}
            )
        }
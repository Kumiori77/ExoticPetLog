from django.urls import path
from . import views

# 유저가 업로드한 파일을 보기위한 설정
from django.conf import settings # 프로젝트 경로의 settings.py 파일
from django.conf.urls.static import static

# 유저가 업로드한 파일을 배포해서 다루기 위해 추가
from django.views.static import serve
from django.urls import re_path


urlpatterns = [
    path("", views.MainView.as_view(), name="main"),
    path("addPet/", views.AddPetView.as_view(), name="addPet"),
    path("recordList/<petID>/", views.RecordListView.as_view(), name="recordList"),
    path("updatePet/<int:pk>/", views.UpdatePetView.as_view(), name="updatePet"),
    path("recording/<int:pk>/", views.RecordView.as_view(), name="recording"),
    path("deletePet/<int:pk>/", views.DeletePetView.as_view(), name="deletePet"),
    path("detailRecord/<int:pk>/", views.RecordDetailView.as_view(), name="detailRecord"),
    path("deleteRecord/<int:pk>/", views.DeleteRecordView.as_view(), name="deleteRecord"),
    path("updateRecord/<int:pk>/", views.UpdateRecordView.as_view(), name="updateRecord"),
    path("graph/<int:pk>/", views.GraphView.as_view(), name="graph"),
    re_path(r'^media/(?P<path>.*)$', serve, {"document_root" : settings.MEDIA_ROOT})
]

# 유저가 업로드한 파일을 보기위한 설정
# 베포할 때는 필요없어서 주석 처리
# urlpatterns += static(
#     prefix=settings.MEDIA_URL,
#     document_root = settings.MEDIA_ROOT,
# )


app_name="record"
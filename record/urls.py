from django.urls import path
from . import views

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
]

app_name="record"
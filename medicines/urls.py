from django.urls import path

from . import views

urlpatterns = [
    path('', views.medicine_list_view, name='medicine_list'),
    path('<int:pk>/', views.medicine_detail_view, name='medicine_detail'),
    path("prescription/upload/", views.prescription_upload, name="prescription_upload"),
    path("prescription/result/", views.prescription_result, name="prescription_result"),
]

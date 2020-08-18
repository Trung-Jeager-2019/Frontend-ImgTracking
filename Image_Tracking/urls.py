from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload_image/', views.upload_image, name='upload_image'),
    path('select_video/', views.select_video, name='select_video'),
    path('upload_video/', views.upload_video, name='upload_video'),
    path('result/', views.result, name='result'),
]
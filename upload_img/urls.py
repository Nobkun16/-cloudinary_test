from django.urls import path
from . import views

urlpatterns=[
    path('', views.upload_img, name="upload_img")

]
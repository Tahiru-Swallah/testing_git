from django.urls import path, re_path
from .views import toy_detail, toy_list

urlpatterns = [
    path('toys/', toy_list, name='toy_list'),
    path('toys/<pk>/', toy_detail, name='toy_detail')
]
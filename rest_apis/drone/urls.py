from django.urls import path
from .views import DroneCategoryDetail, DroneCategoryList, PilotDetail, PilotList, DroneDetail, DroneList, CompetitionDetail, CompetitionList, ApiRoot

urlpatterns = [
    path('drone-categories/', DroneCategoryList.as_view(), name='dronecategory-list'),
    path('drone-categories/<int:pk>/', DroneCategoryDetail.as_view(), name='dronecategory-detail'),
    path('drones/', DroneList.as_view(), name='drone-list'),
    path('drones/<int:pk>/', DroneDetail.as_view(), name='drone-detail'),
    path('pilots/', PilotList.as_view(), name='pilot-list'),
    path('pilots/<int:pk>/', PilotDetail.as_view(), name='pilot-detail'),
    path('competitions/', CompetitionList.as_view(), name='competition-list'),
    path('competitions/<int:pk>/', CompetitionDetail.as_view(), name='competition-detail'),
    path('api-root/', ApiRoot.as_view(), name='api-root')
]
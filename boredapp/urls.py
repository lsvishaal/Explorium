#boredapp
from django.urls import path
from .views import index, suggest_activity
from .api import get_random_activity, filter_activities, get_activity_by_key

urlpatterns = [
    path('', index, name='index'),
    path('suggest_activity/', suggest_activity, name='suggest_activity'),
    path('api/random_activity/', get_random_activity, name='get_random_activity'),
    path('api/filter_activities/', filter_activities, name='filter_activities'),
    path('api/activity/<str:key>/', get_activity_by_key, name='activity_by_key'),
]

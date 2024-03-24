#boredproject
from django.contrib import admin
from django.urls import path, include
from boredapp.views import index, suggest_activity, empty_favicon  # Import empty_favicon here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),  # Include this line to map the root URL to the index view
    path('suggest_activity/', suggest_activity, name='suggest_activity'),
    path('favicon.ico', empty_favicon),  # Define the favicon path here
]

from django.urls import path
from . import views
from weather_api.views import ApiData

urlpatterns = [
    path('', views.get_json_api),  #the path for our get_json_api view

]

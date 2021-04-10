from django.urls import include, path
from data_management.views import *



app_name = "data_management"

urlpatterns = [
	path('search',index, name="index"),
	path('search-data',search_data, name="search_data"),


]

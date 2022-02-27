
from django.urls import path
from . import views

urlpatterns = [
    path('', views.search, name="index"),
    path('search-history/', views.search_history),
]
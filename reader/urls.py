
from django.urls import path
from reader import views


urlpatterns = [
    path('home', views.home, name="Home"),
    path('content', views.loadcontent, name="Loadcontent"),
]
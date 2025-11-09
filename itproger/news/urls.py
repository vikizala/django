from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_news, name='home_news')
]

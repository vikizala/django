from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('about_2', views.about_2, name='about_2'),
    path('about_3', views.about_3, name='about_3')
]


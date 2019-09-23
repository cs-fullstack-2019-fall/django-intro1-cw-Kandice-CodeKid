from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('music/', views.music),
    path('artist1/', views.artist1),
    path('artist2/', views.artist2),
    path('artist3/', views.artist3),
]
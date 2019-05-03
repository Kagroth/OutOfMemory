from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.testApiCall, name='testApiCall'),
    path('register/', views.testApiCall)
]

from django.urls import path
from snippets import views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.testApiCall, name='testApiCall'),
    path('register/', views.testApiCall),
    path('snippetstest/', views.snippet_list),
    path('snippetstest/<int:pk>/', views.snippet_detail),
]

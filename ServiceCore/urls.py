from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.testApiCall, name='testApiCall'),
    path('register/', views.testApiCall),
    path('snippetstest/', views.snippet_list),
    path('snippetstest/<int:pk>/', views.snippet_detail),
    path('user/', views.ProfileRecordView.as_view()),
    path('post/', views.PostView.as_view()),
   #path('hello/', views.HelloView.as_view())
]

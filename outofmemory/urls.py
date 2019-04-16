
from django import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login_user/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logout'),
]



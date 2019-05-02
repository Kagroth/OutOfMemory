from django.urls import path
from django.conf.urls import url, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^register/$', views.CreateUserView.as_view(), name='user'),
]

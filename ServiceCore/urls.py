from django.urls import path
from django.conf.urls import url, include

from . import views
from rest_framework import routers

# from . import api


#router = routers.DefaultRouter()
#router.register(r'register', views.User, 'list')

urlpatterns = [

    path('', views.index, name='index'),
 #   url(r'^api/', include(router.urls)),
  #  url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^register/$', views.CreateUserView.as_view(), name='user'),
]

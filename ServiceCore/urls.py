from django.urls import path
from django.conf.urls import include, url
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.testApiCall, name='testApiCall'),
    path('register/', views.testApiCall),
    path('snippetstest/', views.snippet_list),
    path('snippetstest/<int:pk>/', views.snippet_detail),
    path('user/', views.ProfileRecordView.as_view()),
    path('post/', views.PostView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

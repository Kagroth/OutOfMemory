from django.urls import path
from django.conf.urls import include, url
from . import views
from .views import HelloView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('user/', views.ProfileRecordView.as_view()),
    path('post/', views.PostView.as_view()),
    path('post/search/', views.PostViewFilter.as_view()),
    path('post/new/', views.PostCreate.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

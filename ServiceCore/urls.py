from django.urls import path
from django.conf.urls import include, url
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('profile/', views.ProfileRecordView.as_view()),
    path('profile/cv/', views.CVView.as_view()),
    path('post_preview/', views.PostPreviewView.as_view()),
    path('post/', views.PostView.as_view()),
    path('post/search/', views.PostViewFilter.as_view()),
    path('post/tag/<str:tag>', views.PostPreviewByTagFilterView.as_view()),
    path('post/new/', views.PostCreate.as_view()),
    path('post/details/<int:pk>', views.PostDetailsView.as_view()),
    path('post/comment/new/', views.CommentView.as_view()),
    path('post/comment/<int:pk>', views.RateCommentView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('job/', views.JobOffersPreviewView.as_view()),
]

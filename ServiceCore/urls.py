from django.urls import path
from django.conf.urls import include, url

from ServiceCore.views import ProfileAvatarUpload
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf.urls.static import static
from django.conf import settings

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
    path('job/new/', views.JobOfferCreateView.as_view()),
    path('job/edit/<int:pk>', views.JobOfferEditView.as_view()),
    path('job/details/<int:pk>', views.JobOfferDetailsView.as_view()),
    path('job/<int:pk>/applications', views.ApplicationView.as_view()),
    path('tag/', views.TagView.as_view()),
    url(r'^upload/(?P<filename>[^/]+)$', ProfileAvatarUpload.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

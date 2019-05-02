from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import User, UserSerializer


# Create your views here.

def index(request):
    return HttpResponse("Hello world")


class CreateUserView(CreateAPIView):
    model = User
    permission_classes = (AllowAny)
    serializer_class = UserSerializer

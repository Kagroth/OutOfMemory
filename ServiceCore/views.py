from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import CreateAPIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


# Create your views here.

def index(request):
    return HttpResponse("Hello world")


class ViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)


class CreateUserView(CreateAPIView):
    model = USer
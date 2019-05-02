from django.http import HttpResponse
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from .serializers import User, UserSerializer


# Create your views here.

def index(request):
    return HttpResponse("Hello world")


class CreateUserView(CreateAPIView):
    model = User
    permission_classes = (AllowAny)
    serializer_class = UserSerializer

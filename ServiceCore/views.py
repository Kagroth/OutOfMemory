from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import never_cache
import json

from rest_framework.parsers import JSONParser


from ServiceCore.serializers import *
from ServiceCore.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

def index(request):
    return HttpResponse("Hello world")

@csrf_exempt
@never_cache
def testApiCall(request):
    content = {}
    if request.method == "POST":
        content = json.loads(request.body)

    print(content)
    return JsonResponse({"content": content})


@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)



class ProfileRecordView(APIView):
    
    def get(self, format=None):
        """
        Get all the profile records
        """
        users = Profile.objects.all()
        serializer = ProfileSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a profile record
        """
        requestedData = JSONParser().parse(request)

        serializer = UserSerializer(data=requestedData)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=requestedData)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)

class PostView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializedPosts = PostSerializer(posts, many=True)
        return Response(serializedPosts.data)
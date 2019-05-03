from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import never_cache
import json

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


from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import never_cache
import json

# Create your views here.

def index(request):
    return render(request, 'servicecore/index.html')

@csrf_exempt
@never_cache
def testApiCall(request):
    content = {}
    if request.method == "POST":
        content = json.loads(request.body)

    print(content)
    return JsonResponse({"content": content})
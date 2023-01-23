from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

import json
def myfun(request):
    py_dict={'wish':'hello world'}
    json_resp=json.dumps(py_dict)
    return HttpResponse(json_resp)
  
def wish(request):
    return HttpResponse("<h1>iam from wish</h1>")
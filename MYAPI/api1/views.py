import json
from django.shortcuts import render
import io

def student_api(request):
    if request.method == "GET":
        json_data= request.body
        strem=io.byteIO(json_data)


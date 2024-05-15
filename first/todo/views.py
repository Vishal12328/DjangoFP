from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
tasks = ["eat","sleep","repeat"]
def index(request):
    return render(request,"todo/tasklist.html",{
        "tasks":tasks
    })
def add(request):
    return render(request,"todo/add.html")
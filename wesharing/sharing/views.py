from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'sharing/index.html')

def upload(request):
    return render(request, 'sharing/index.html')

def download(request):
    return render(request, 'sharing/download.html')

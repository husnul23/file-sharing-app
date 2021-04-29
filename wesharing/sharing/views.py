from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import File
from .forms import UploadForm

def index(request):
    return render(request, 'sharing/index.html')

def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            return HttpResponseRedirect('/download/')

    return render(request, 'sharing/index.html')

def download(request):
    return render(request, 'sharing/download.html')

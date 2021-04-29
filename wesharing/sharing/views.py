import uuid
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
            formfile = form.save(commit=False) #save on memory, but not on database
            uid = uuid.uuid1()
            formfile.uid = str(uid) # using str, because uid is object, and formfile.uid is string
            formfile.save()

            return HttpResponseRedirect('/' + formfile.uid)

    return render(request, 'sharing/index.html')

def download(request, uid):
    return render(request, 'sharing/download.html')

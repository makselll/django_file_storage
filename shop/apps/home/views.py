from django.shortcuts import render
from acc.models import *



def index(request):
    all_documents = Document.objects.all().exclude(private = True)
    return render(request, 'home/home.html', context={'mydocuments':all_documents})



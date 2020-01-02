from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import *
from .forms import UploadFileForm
from home.views import *


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid login or password')
            return redirect('/acc/login')
    else:
        return render(request, 'acc/login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.info(request, 'Username taken')
                return redirect('/acc/register')
            elif User.objects.filter(email = email).exists():
                messages.info(request, 'Email taken')
                return redirect('/acc/register')
            else:
                user = User.objects.create_user(username = username, password=password1, email = email, first_name = first_name, last_name = last_name)
                user.save()
                return redirect('/acc/login')
        else:
            messages.info(request, 'Pass != Pass 2')
        return redirect('/acc/register')
    else:

        return render(request, 'acc/register.html')


def profile(request):
    mydocuments = Document.objects.all().filter(user = auth.get_user(request))
    return render(request, 'acc/profile.html', context={'mydocuments': mydocuments})


def update_document(request, id = None):
    document = Document.objects.get(id=id)
    print(document)
    print(request.POST)
    privat = request.POST.get('privat')
    description = request.POST.get('desc')
    document.private = privat
    document.description = description
    document.save()
    return redirect('/acc/profile')


def delete_document(request, id=None):
    print(id)
    Document.objects.get(id = id).delete()
    return redirect('/acc/profile')


def update_points(request, id = None):
    if request.method == 'POST':
        document = Document.objects.get(id = id)
        point = request.POST.get('point')
        if point == '1':
            created = PostLikes.objects.get_or_create(user=auth.get_user(request), document=document)
            created[0].value = int(point)
            created[0].save()
            return redirect('/')

        else:
            created = PostLikes.objects.get_or_create(user=auth.get_user(request), document=document)
            created[0].value = int(point)
            created[0].save()
            return redirect('/')
    else: 
        return redirect('/')

    return render(request, 'acc/profile.html')


def save_doc(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            title = form.cleaned_data['title']
            file = form.cleaned_data['file']
            description = form.cleaned_data['description']
            private = form.cleaned_data['private']
            Document.objects.create(title=title, user=auth.get_user(request), file=file, description=description, private=private, score=0)
            return redirect('/acc/profile')
    else:
        form = UploadFileForm()
    return render(request, 'acc/create_doc.html', {'form': form})




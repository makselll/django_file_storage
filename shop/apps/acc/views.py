from django.shortcuts import redirect
from django.contrib.auth.models import auth
from .models import *
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, View
from django.urls import reverse_lazy


class ProfileDetailView(ListView):
    template_name = 'acc/profile.html'

    def get_queryset(self):
        return Document.objects.filter(user=self.request.user)


class UpdateDataDocumentView(UpdateView):
    model = Document
    fields = ['title', 'description', 'file', 'private']
    success_url = reverse_lazy('profile')


class DeleteDocumentView(DeleteView):
    model = Document
    success_url = reverse_lazy('profile')


class NewDocumentView(CreateView):
    model = Document
    fields = ['title', 'description', 'file', 'private']
    template_name = 'acc/create_doc.html'
    success_url = reverse_lazy('profile')

    def form_valid (self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(NewDocumentView, self).form_valid(form)


class UpdateScoreDocumentView(View):
    def post(self, request, id):
        document = Document.objects.get(id=id)
        point = int(request.POST.get('point'))
        find_or_create_postlike = PostLikes.objects.get_or_create(user=auth.get_user(request), document=document)
        find_or_create_postlike[0].value = point
        find_or_create_postlike[0].save()
        return redirect(reverse_lazy('home'))


class HomeListView(ListView):
    queryset = Document.objects.filter(private = False)
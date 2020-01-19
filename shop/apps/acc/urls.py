from django.urls import path, include
from .views import ProfileDetailView, UpdateDataDocumentView, DeleteDocumentView, NewDocumentView, UpdateScoreDocumentView
from . import views


urlpatterns =[
    path('', ProfileDetailView.as_view(), name='profile'),
    path('update/<int:pk>', UpdateDataDocumentView.as_view(), name='update_document'),
    path('delete/<int:pk>/', DeleteDocumentView.as_view(), name='delete_document'),
    path('points/<int:id>/', UpdateScoreDocumentView.as_view(), name='update_points'),
    path('new/', NewDocumentView.as_view(), name='new_document'),

]
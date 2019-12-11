from django.urls import path, include
from . import views


urlpatterns =[
    path('register/', views.register, name = 'register'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
    path('profile/', views.profile, name = 'profile'),
    path('edit/<int:id>/', views.update_document, name='update_document'),
    path('delete/<int:id>/', views.delete_document, name='delete_document'),
    path('points/<int:id>/', views.update_points, name='update_points'),
    path('save_doc/', views.save_doc, name='save_doc'),

]
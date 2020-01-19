from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from acc.views import HomeListView
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('allauth.urls')),
    path('', HomeListView.as_view(), name='home'),
    # Apps
    path('acc/', include('acc.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

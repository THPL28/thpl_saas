# thpl_saas/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls')),  # Inclui as URLs do app 'projects'
]

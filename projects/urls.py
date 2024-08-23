# projects/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # URL para a view 'home'
    path('projects/', views.project_list, name='project_list'),
    path('about/', views.about, name='about'),  
    path('contact/', views.contact_view, name='contact'),
     path('under-development/', views.under_development, name='under_development'),
]

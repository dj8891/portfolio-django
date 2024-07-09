from django.urls import path
from . import views

urlpatterns = [
  path('usages/', views.get_usages, name='get_usages'),
  path('jobs/', views.get_jobs, name='get_jobs'),
  path('projects/', views.get_projects, name="get_projects")
]
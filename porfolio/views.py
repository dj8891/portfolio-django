from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Jobs, Projects, Usages
from django.http import JsonResponse
from django.db.models import F

@api_view(['GET'])
def get_usages(request):
  usages = Usages.objects.prefetch_related('tools').values('id', 'techTitle', 'tools__id', 'tools__url', 'tools__tool', 'tools__desc', 'tools__href')
  result_dict = {}
  for usage in usages:
    usage_id = usage['id']
    if usage_id not in result_dict:
      result_dict[usage_id] = {
        'id': usage['id'],
        'techTitle': usage['techTitle'],
        'tools': []
      }
    
    tool = {
        'id': usage['tools__id'],
        'url': usage['tools__url'],
        'tool': usage['tools__tool'],
        'desc': usage['tools__desc'],
        'href': usage['tools__href']
    }
    
    result_dict[usage_id]['tools'].append(tool)

  result_list = list(result_dict.values())
  return JsonResponse(result_list, safe=False)

def get_jobs(request):
  jobs = Jobs.objects.values()
  return JsonResponse(list(jobs), safe=False)

def get_projects(request):
  projects = Projects.objects.values()
  return JsonResponse(list(projects), safe=False)
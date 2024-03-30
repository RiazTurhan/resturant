from django.shortcuts import render
from . import models

def service(request):
  
  data = models.service_data.objects.order_by('-id')[:6]

  forFile = {
    'services_data': data
  }
  
  return render(request, 'serv/service.html', forFile)
# Create your views here.

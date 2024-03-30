from django.shortcuts import render
from serv.models import service_data

def home(request):

  service_datas = service_data.objects.order_by('-id')[:4]

  all_data = {
    'services_data': service_datas
  }
  return render (request,'home/index.html', all_data )

# Create your views here.

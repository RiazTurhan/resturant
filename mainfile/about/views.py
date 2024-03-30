from django.shortcuts import render
from . import models

def about(request):

  all_about = models.about_data.objects.get()
  members_Data = models.members.objects.all()

  data = {
    'about' : all_about,
    'member': members_Data
  }
  return render (request, 'about/about.html', data)
# Create your views here.

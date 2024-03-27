from django.shortcuts import render


def book(request):
  return render(request, 'pages_sec/booking.html')

def team(request):
  return render(request, 'pages_sec/team.html')


def test(request):
  return render(request, 'pages_sec/testimonial.html')
# Create your views here.

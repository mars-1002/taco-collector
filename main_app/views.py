from django.shortcuts import render
from .models import Taco

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def taco_index(request):
  tacos =  Taco.objects.all()
  return render(request, 'tacos/index.html', { 'tacos': tacos })

def taco_detail(request, taco_id):
  taco = Taco.objects.get(id=taco_id)
  return render(request, 'tacos/detail.html', { 'taco': taco })
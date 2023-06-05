from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

class TacoCreate(CreateView):
  model = Taco
  fields = '__all__'
  success_url = '/tacos/'

class TacoUpdate(UpdateView):
  model = Taco
  fields = ['meat', 'description', 'order']

class TacoDelete(DeleteView):
  model = Taco
  success_url = '/tacos/'
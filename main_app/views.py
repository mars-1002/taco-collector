from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Taco
from .forms import FeedingForm

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def taco_index(request):
  tacos =  Taco.objects.all()
  return render(request, 'tacos/index.html', { 'tacos': tacos })

def taco_detail(request, taco_id):
  taco = Taco.objects.get(id=taco_id)
  feeding_form = FeedingForm()
  return render(request, 'tacos/detail.html', { 
    'taco': taco,
    'feeding_form': feeding_form
  })

def add_feeding(request, taco_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.taco_id = taco_id
    new_feeding.save()
  return redirect('taco-detail', taco_id=taco_id)

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


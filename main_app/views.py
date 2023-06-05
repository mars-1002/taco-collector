from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Taco, Sauce
from .forms import FeedingForm
from django.views.generic import ListView, DetailView

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def taco_index(request):
  tacos =  Taco.objects.all()
  return render(request, 'tacos/index.html', { 'tacos': tacos })

def taco_detail(request, taco_id):
  taco = Taco.objects.get(id=taco_id)
  sauces_taco_doesnt_have = Sauce.objects.exclude(id__in = taco.sauces.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'tacos/detail.html', { 
    'taco': taco,
    'feeding_form': feeding_form,
    'sauces': sauces_taco_doesnt_have
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
  fields = 'name', 'meat', 'description', 'order'
  success_url = '/tacos/'

class TacoUpdate(UpdateView):
  model = Taco
  fields = ['meat', 'description', 'order']

class TacoDelete(DeleteView):
  model = Taco
  success_url = '/tacos/'

class SauceCreate(CreateView):
  model = Sauce
  fields = '__all__'

class SauceList(ListView):
  model = Sauce

class SauceDetail(DetailView):
  model = Sauce

class SauceUpdate(UpdateView):
  model = Sauce
  fields = ['name', 'color']

class SauceDelete(DeleteView):
  model = Sauce
  success_url = '/sauces/'

def assoc_sauce(request, taco_id, sauce_id):
  Taco.objects.get(id=taco_id).sauces.add(sauce_id)
  return redirect('taco-detail', taco_id=taco_id)
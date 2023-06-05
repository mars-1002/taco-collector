from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('tacos/', views.taco_index, name='taco-index'),
  path('tacos/<int:taco_id>/', views.taco_detail, name="taco-detail"),
]
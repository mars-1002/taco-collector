from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('tacos/', views.taco_index, name='taco-index'),
  path('tacos/<int:taco_id>/', views.taco_detail, name="taco-detail"),
  path('tacos/create', views.TacoCreate.as_view(), name='taco-create'),
  path('tacos/<int:pk>/update/', views.TacoUpdate.as_view(), name='taco-update'),
  path('tacos/<int:pk>/delete/', views.TacoDelete.as_view(), name='taco-delete'),
  path('tacos/<int:taco_id>/add-feeding', views.add_feeding, name='add-feeding'),
]
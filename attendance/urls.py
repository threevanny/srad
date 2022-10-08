from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'), # login page
  path('exit/', views.exit, name='exit'), # logout page
  path('marks/', views.marks, name='marks'),
  path('difficulties/', views.difficulties, name='difficulties'),
  path('dashboard/', views.dashboard, name='dashboard'),

]

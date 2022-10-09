import datetime
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Class, Report
from csv import reader
from django.contrib.auth.models import User
from django.http import JsonResponse

# Create your views here.

# login view and user authentication
def home(request):
  # before all, check if user is already logged in
  if request.user.is_authenticated:
    return redirect('marks')
  

  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect('marks') # Redirect to a success page.
    else:
      messages.error(request, 'Oops! Authentication failed. Please try again.')
      return redirect('home') # Return an 'invalid login' error message.
  else:
    return render(request, 'home.html', {})

# logout view
def exit(request):
  logout(request) 
  return redirect('home')

@login_required(login_url='home')
def marks(request):
  if request.user.is_staff:
    return redirect('dashboard')

  day = getDay()
  date = getDate()
  # get classes where teacher is assigned and day is today
  classes = Class.objects.filter(teacher=request.user, day=day).order_by('start_time')
  return render(request, 'marks.html', {'classes': classes, 'day': day, 'date': date})

@login_required(login_url='home')
def difficulties(request):
  return render(request, 'difficulties.html')

@staff_member_required
def dashboard(request):
  return render(request, 'dashboard.html')




def getDay():
  # get day from server
  day = datetime.datetime.now().strftime("%A")

  if(day == 'Sunday'):
    day = 'DOMINGO'
  elif(day == 'Monday'):
    day = 'LUNES'
  elif(day == 'Tuesday'):
    day = 'MARTES'
  elif(day == 'Wednesday'):
    day = 'MIERCOLES'
  elif(day == 'Thursday'):
    day = 'JUEVES'
  elif(day == 'Friday'):
    day = 'VIERNES'
  elif(day == 'Saturday'):
    day = 'SABADO'
  
  return day

def getDate():
  # get date from server
  date = datetime.datetime.now().strftime("%x")
  return date

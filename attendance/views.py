from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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

def marks(request):
  return render(request, 'marks.html')

def difficulties(request):
  return render(request, 'difficulties.html')

def dashboard(request):
  return render(request, 'dashboard.html')




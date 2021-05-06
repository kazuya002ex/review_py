from django.shortcuts import render

def signupview(request):
  return render(request, 'signup.html', { 'somedata' : 100 })

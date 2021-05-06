from django.shortcuts import render

def signupview(request):
  if request.method == 'POST':
    print('POST method')
  else:
    print('GET method probably...')
  return render(request, 'signup.html', {})

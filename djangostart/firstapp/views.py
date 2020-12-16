from django.shortcuts import render

# Create your views here.

students = ['최주원', '세종대왕', '고재증']

def home(request):
  context = {
    'user_chat': 'hello',
    'user_name': 'jaejeung'
  }
  return render(request, 'home.html', context)

def result(request):
  name = request.POST['username']

  if name in students:
    is_exist = True
  else :
    is_exist = False

  context ={
    'user_name':name,
    'is_exist': is_exist
  }
  return render(request, 'result.html', context)
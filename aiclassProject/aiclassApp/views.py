from django.shortcuts import render, redirect
from .models import AiClass, AiStudents

# Create your views here.

def home(request):
  classes = AiClass.objects.all()
  context = {
    'classes' : classes
  }
  return render(request, 'home.html', context)

def detail(request, class_pk):
  # print('🥇',class_pk)
  class_obj = AiClass.objects.get(pk=class_pk)
  student_obj = AiStudents.objects.filter(class_num=class_pk)

  context = {
    'class_pk': class_pk,
    'class_obj': class_obj,
    'student_obj': student_obj
  }

  return render(request, 'detail.html', context)

def add(request, class_pk):
  print('🥇', class_pk)
  class_obj = AiClass.objects.get(pk=class_pk)

  if request.method == 'POST':
    AiStudents.objects.create(
      class_num = class_pk,
      name = request.POST['name'],
      phone_num = request.POST['phone_num'],
      intro_text = request.POST['intro_text']
    )

    return redirect('detail', class_pk)

  context = {
    'class_obj': class_obj
  }
  return render(request, 'add.html', context)
from django.shortcuts import render, redirect
from .models import AiClass, AiStudents
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
ERROR_MSG = {
    'ID_EXIST' : '이미 사용 중인 아이디 입니다.',
    'ID_NOT_EXIST' : '존재하지 않는 아이디 입니다.',
    'ID_PW_MISSING' : '아이디와 비밀번호를 다시 확인해주세요.',
    'PW_CHECK' : '비밀번호가 일치하지 않습니다.'
}

def home(request):
    class_obj_list = AiClass.objects.all()
    context = {
        'class_obj_list':class_obj_list
    }
    return render(request, 'home.html', context)

def detail(request, class_pk):
    print(class_pk)

    class_obj = AiClass.objects.get(pk=class_pk)
    students_obj = AiStudents.objects.filter(class_num=class_pk)

    context = {
        'class_pk':class_pk,
        'class_obj':class_obj,
        'student_obj':students_obj
    }
    return render(request, 'detail.html', context)

def add(request, class_pk):
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
        'class_obj':class_obj
    }
    return render(request, 'add.html',context)

def student(request, student_pk):
    student = AiStudents.objects.get(pk=student_pk)
    context = {
        'student':student
    }
    return render(request, 'student.html', context)

def edit(request, student_pk):
    if request.method == 'POST':
        AiStudents.objects.filter(pk=student_pk).update(
            name=request.POST['name'],
            phone_num=request.POST['phone_num'],
            intro_text=request.POST['intro_text']
        )
        return redirect('student', student_pk)

    student = AiStudents.objects.get(pk=student_pk)
    context = {
        'student' : student
    }
    return render(request, 'edit.html',context)

def delete(request, class_num ,student_pk):
    target_student = AiStudents.objects.get(pk=student_pk)
    target_student.delete()

    class_pk = class_num
    return redirect('detail', class_pk)

def signup(request):
    context = {
        'error':{
            'state':False,
            'msg':''
        }
    }
    if request.method == 'POST':
        user_id = request.POST['user_id']
        user_pw = request.POST['user_pw']
        user_pw_check = request.POST['user_pw_check']

        user = User.objects.filter(username=user_id)

        if (user_id and user_pw):
            # 존재하지 않는 아이디라면.
            if len(user) == 0:
                if (user_pw == user_pw_check):
                    user = User.objects.create_user(
                        username=user_id,
                        password=user_pw
                    )

                    auth.login(request, user)

                    return redirect('home')

                else :
                    context['error']['state'] = True
                    context['error']['msg'] = ERROR_MSG['PW_CHECK']
            else :
                context['error']['state'] = True
                context['error']['msg'] = ERROR_MSG['ID_EXIST']
        else:
            context['error']['state'] = True
            context['error']['msg'] = ERROR_MSG['ID_PW_MISSING']

    return render(request, 'signup.html', context)

def login(request):
    context = {
        "error":{
            "state" : False,
            "msg" : ""
        }
    }

    if request.method == 'POST':
        user_id = request.POST['user_id']
        user_pw = request.POST['user_pw']

        user = User.objects.filter(username=user_id)

        if (user_id and user_pw):
            # 존재하는 아이디라면,
            if len(user) != 0:
                user = auth.authenticate(
                    username = user_id,
                    password = user_pw
                )
                
                if user != None:
                    auth.login(request, user)

                    return redirect('home')
                else:
                    context['error']['state'] = True
                    context['error']['msg'] = ERROR_MSG['PW_CHECK']

            else:
                context['error']['state'] = True
                context['error']['msg'] = ERROR_MSG['ID_NOT_EXIST']
        else:
            context['error']['state'] = True
            context['error']['msg'] = ERROR_MSG['ID_PW_MISSING']

    return render(request, 'login.html', context)

def logout(request):
    if request.method == "POST":
        auth.logout(request)

    return redirect('home')
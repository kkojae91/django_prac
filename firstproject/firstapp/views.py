from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
students = ['고재증','홍길동','최주원','세종대왕']
def home(request):
    return render(request, 'home.html')

def result(request):
    name = request.POST['user_name']

    if name in students:
        is_exist = True
    else:
        is_exist = False
    return render(request, 'result.html',{'user_name':name,'is_exist':is_exist})
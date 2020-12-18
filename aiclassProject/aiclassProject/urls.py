"""aiclassProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from aiclassApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('detail/<int:class_pk>', views.detail, name='detail'),
    path('add/<int:class_pk>', views.add, name='add'),
    path('student/<int:student_pk>', views.student, name='student'),
    path('edit/<int:student_pk>', views.edit, name='edit'),
    path('student/<int:class_num>/<int:student_pk>', views.delete, name='delete'),
]

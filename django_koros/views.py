from django.shortcuts import render
from .form import EmpForm


def Home(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'aboutus.html')


def contact(request):
    return render(request, 'contactus.html')


def myform(request):
    stu = EmpForm
    return render(request, 'forms.html', {'form': stu})

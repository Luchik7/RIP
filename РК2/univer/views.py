from django.shortcuts import render
from .models import *

# Create your views here.

def students(request):
    context = {
        'students': Student.objects.all()
    }
    return render(request, 'univer/students.html', context)
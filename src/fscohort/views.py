from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

def main_view(request):
    return render(request, 'fscohort/main.html')

def home_view(request):
    return HttpResponse('<h1>HomePage')


def student_list(request):
    students = Student.objects.all()
    num_of_students = Student.objects.count()
    context = {
        'students' : students,
        'number' : num_of_students
    }
    return render(request, 'fscohort/student.html', context)


# Create your views here.

from django.shortcuts import render
from .models import Student

def table_view(request):
    students = Student.objects.all()
    return render(request, 'tableapp/table.html', {"students": students})

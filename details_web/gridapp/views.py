from django.shortcuts import render, redirect
from .models import Student

def grid(request):
    return render(request, 'gridapp/grid.html')

def carousel(request):
    return render(request, 'gridapp/carousel.html')

def table(request):
    return render(request, 'gridapp/table.html')


def student_view(request):
    if request.method == "POST":
        name = request.POST['name']
        course = request.POST['course']

        Student.objects.create(name=name, course=course)

        return redirect('students')

    students = Student.objects.all()
    return render(request, 'gridapp/students.html', {'students': students})
from django.shortcuts import redirect, get_object_or_404


def student_list(request):
    if request.method == "POST":
        name = request.POST['name']
        course = request.POST['course']
        Student.objects.create(name=name, course=course)
        return redirect('students')

    students = Student.objects.all()
    return render(request, 'gridapp/students.html', {'students': students})


def update_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.name = request.POST['name']
        student.course = request.POST['course']
        student.save()
        return redirect('students')

    return render(request, 'gridapp/update.html', {'student': student})


def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('students')

def set_session(request):
    request.session['username'] = "Pranitha"
    return render(request, 'gridapp/session.html')


def get_session(request):
    username = request.session.get('username')
    return render(request, 'gridapp/session.html', {'username': username})


def set_cookie(request):
    response = render(request, 'gridapp/cookie.html')
    response.set_cookie('course', 'BTech')
    return response


def get_cookie(request):
    course = request.COOKIES.get('course')
    return render(request, 'gridapp/cookie.html', {'course': course})
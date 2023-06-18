from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .forms import *
from .models import Student, Teacher, Course, Attendance, Grade, Material, Schedule, Payment


def user(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Успешно!!!')
    context = {'form': form}
    return render(request, 'index.html', context)

def enroll(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Вы успешно зарегистирровались! Оплатите курс с помощью данного реквизита: "1200056156" и отправьте чек по данной ссылке https://t.me/+Vy5pKL4hZhO1jvKH')
    context = {'form': form}
    return render(request, 'payment.html', context)

def teacher(request):
    form = TeacherForm()
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Успешно!!!')
    context = {'form': form}
    return render(request, 'employee.html', context)

def assessment(request):
    if request.method == 'POST':
        form = AssessmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Сохранение данных формы в базе данных
            return HttpResponse('success')  # Перенаправление на страницу успешного завершения
    else:
        form = AssessmentForm()

    context = {
        'form': form
    }
    return render(request, 'assessment.html', context)


class StudentList(generic.ListView):
    model = Student
    template_name = 'student_list.html'

class TeacherList(generic.ListView):
    model = Teacher
    template_name = 'teacher_list.html'

class AboutList(generic.ListView):
    model = Teacher
    template_name = 'about_list.html'

class BlogsList(generic.ListView):
    model = Material
    template_name = 'blogs_list.html'

class PostList(generic.ListView):
    model = Material
    template_name = 'post_list.html'

class EngTestList(generic.ListView):
    model = Material
    template_name = 'eng-test_list.html'

class CoursesList(generic.ListView):
    model = Course
    template_name = 'courses_list.html'

class CourseInnerList(generic.ListView):
    model = Course
    template_name = 'course-inner_list.html'


class CourseInnerIndividualList(generic.ListView):
    model = Course
    template_name = 'course-inner_individual_list.html'


class ContactList(generic.ListView):
    model = Material
    template_name = 'contact_list.html'
from collections import Set

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from home.forms import SignUpForm, CourseForm
from home.models import Course, Student


def homePage(request):
    return render(request, 'home.html', {'register_button': True, 'sign_in_button': True, 'exit_button': False})


def add_course_page(request):
    form = CourseForm()
    if request.method == "POST":
        form = CourseForm(request.POST)
        form.save()
    return render(request, 'add_course.html')


def add_course(request):
    return render(request, 'add_course.html')


def register_course(request, course_number, group_number):
    course_number = int(course_number)
    group_number = int(group_number)
    course = Course.objects.filter(course_number=course_number, group_number=group_number).first()
    request.user.student.courses.add(course)
    return redirect("/all_courses")


def register(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            student = Student()
            student.user = user
            student.save()
    return render(request, 'register.html',
                  {'form': form, 'register_button': True, 'sign_in_button': True, 'exit_button': False})


def sign_in(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, 'sign_in.html',
                          {'valid': False, 'register_button': True, 'sign_in_button': True, 'exit_button': False})
    return render(request, 'sign_in.html', {'valid': True})


def contact_us_done(request):
    flag = True
    text = request.POST['text']
    if len(text) > 250:
        flag = False
    if len(text) < 10:
        flag = False
    if flag:
        send_mail(
            request.POST['title'],
            request.POST['email'] + "\n" + text,
            'joorabnakhi@gmail.com',
            ['webe19lopers@gmail.com']
        )
        return render(request, 'contact_us_done.html')
    else:
        return redirect("contact_us")


def login_view(request):
    return render(request, 'logged_in.html',
                  {'register_button': False, 'sign_in_button': False, 'exit_button': True})


def logout_view(request):
    logout(request)
    return redirect("/")


def edit_profile_done(request):
    if request.POST:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        photo = request.FILES.get('photo')
        if first_name != "":
            request.user.first_name = first_name
        if last_name != "":
            request.user.last_name = last_name
        if photo:
            student = Student.objects.get(user=request.user)
            student.profile_photo = photo
            student.save()
        request.user.save()
    return profile(request)


def edit_profile(request):
    return render(request, 'edit_profile.html')


def panel(request):
    return render(request, 'panel.html')


def contact_us(request):
    return render(request, 'contact_us.html')


def profile(request):
    student = Student.objects.get(user=request.user)
    img = student.profile_photo
    flag = True
    if not img:
        flag = False
    return render(request, 'profile.html', {'img': student.profile_photo, 'flag': flag})


def all_courses(request):
    if not Student.objects.filter(user=request.user):
        student = Student(user=request.user).save()
        print("student created")
    if request.method == 'POST':
        list = []
        query_text = request.POST['search_query']
        for course in Course.objects.all():

            flag = True
            if request.POST.get('teacher'):
                flag = False
                if course.teacher == query_text:
                    list.append(course)
                    continue
            if request.POST.get('course'):
                flag = False
                if course.name == query_text:
                    list.append(course)
                    continue
            if request.POST.get('department') or flag:
                if course.department == query_text:
                    list.append(course)
        courses = list
        search_state = True
    else:
        courses = Course.objects.all()
        search_state = False

    return render(request, 'all_courses.html',
                  {'courses': courses, 'all_courses': all_courses, 'search_state': search_state})

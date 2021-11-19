from django.shortcuts import render


def student_home(request):
    return render(request,"student_template/student_home_template.html")

def course(request):
    return render(request,"student_template/student_course_template.html")
def task1(request):
    return render(request,"student_template/task1.html")
def task2(request):
    return render(request,"student_template/task2.html")
def task3(request):
    return render(request,"student_template/task3.html")
def task4(request):
    return render(request,"student_template/task4.html")
def task5(request):
    return render(request,"student_template/task5.html")
def task6(request):
    return render(request,"student_template/task6.html")
def task7(request):
    return render(request,"student_template/task7.html")
def task8(request):
    return render(request,"student_template/task8.html")


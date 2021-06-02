"""system_school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from system_school import settings
from system_school_app import views

from system_school_app import HodViews

from system_school_app import StudentViews

urlpatterns = [
    path('demo',views.showDemoPage),
    path('admin/', admin.site.urls),
    path('', views.ShowLoginPage),
    path('get_user_details', views.GetUserDetails),
    path('logout_user', views.logout_user, name="logout"),
    path('doLogin', views.doLogin),
    path('admin_home',HodViews.admin_home,name="admin_home"),
    path('add_staff', HodViews.add_staff, name="add_staff"),
    path('add_staff_save', HodViews.add_staff_save, name="add_staff_save"),
    path('student_home', StudentViews.student_home, name="student_home"),
    path('course', StudentViews.course, name="course"),
    path('task1', StudentViews.task1, name="task1"),
    path('task2', StudentViews.task2, name="task2"),
    path('task3', StudentViews.task3, name="task3"),
    path('task4', StudentViews.task4, name="task4"),
    path('task5', StudentViews.task5, name="task5"),
    path('task6', StudentViews.task6, name="task6"),
    path('task7', StudentViews.task7, name="task7"),
    path('task8', StudentViews.task8, name="task8"),

]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)

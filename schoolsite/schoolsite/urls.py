"""schoolsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from users import views as users_views
from school.views import *
from users.views import *
from django.contrib.auth import views as auth_views
from rest_framework import routers

# router_teacher = routers.DefaultRouter()
# router_teacher.register(r'teacher', TeacherViewSet)
# router_student = routers.DefaultRouter()
# router_student.register(r'student', StudentViewSet)

# http://127.0.0.1:8000/api/v1/auth/users/ регистрация пользователя
# http://127.0.0.1:8000/api/v1/drf-auth/login/ вход
# http://127.0.0.1:8000/accounts/profile/ профиль
# http://127.0.0.1:8000/api/v1/drf-auth/logout/ выход
#
#

urlpatterns = [
    path('', main, name='Home'),
    path('admin/', admin.site.urls),
    path('register/', users_views.register, name='register'),
    path('login/', users_views.login_view, name='Login'),
    path('logout/', users_views.logout_view, name='Logout'),
    path('courses/', course_registration, name='courses'),
    path('account/', profile, name='account'),
    path('schedule/', schedule, name='schedule'),
    path('students-courses-report/excel/', students_courses_report, name='students-courses-report-excel'),
    path('students-report/excel/', students_report, name='students-report-excel'),
    path('attendance-and-classes-report/excel/', attendance_and_classes_report, name='attendance-and-classes-report-excel'),
    path('student-performance/excel/', student_performance, name='student-performance'),


    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    # path('api/v1/auth/users/', StudentRegistration, name='Registration'),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    path('teacher/', TeacherAPIList.TeacherList, name='TeacherList'),
    path('api/v1/teacher/<int:pk>/', TeacherAPIUpdate.TeacherUpdate, name='TeacherUpdate'),
    path('api/v1/teacherdelete/<int:pk>/', TeacherAPIDestroy.as_view()),

    # path('api/v1/', include(router_teacher.urls)),
    # path('api/v1/', include(router_student.urls))
    path('download/<path:file_name>/', download_file, name='download_file'),

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



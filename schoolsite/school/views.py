from django.contrib.auth.views import LoginView
from django.forms import model_to_dict
from django.shortcuts import render
from requests import request
from rest_framework import generics
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import Lesson
from .models import Teacher, School
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import TeacherSerializer

def main(request):
        return render(request, 'main.html')

def school_info(request):
    schools = School.objects.get(pk=1)
    return render(request, 'courses.html', {'schools': schools})

class TeacherAPIList(generics.ListCreateAPIView):
     queryset = Teacher.objects.all()
     serializer_class = TeacherSerializer
     permission_classes = (IsAuthenticatedOrReadOnly, )
     def TeacherList(request):
         queryset = Teacher.objects.all()
         return render(request, 'teacher.html', {'queryset': queryset})

class TeacherAPIUpdate(generics.RetrieveUpdateAPIView):
     queryset = Teacher.objects.all()
     serializer_class = TeacherSerializer
     permission_classes = (IsAuthenticated,)
     def TeacherUpdate(request):
         queryset = Teacher.objects.all()
         return render(request, 'index.html', {'queryset': queryset})

class TeacherAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = (IsAdminOrReadOnly, )



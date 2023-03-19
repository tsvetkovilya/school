from django.shortcuts import render
from rest_framework import generics
from .models import Teacher, Student
from .serializers import TeacherSerializer, StudentSerializer



class TeacherAPIView(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class StudentAPIView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
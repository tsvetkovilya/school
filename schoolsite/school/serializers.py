from rest_framework import serializers

from .models import Teacher
from .models import Student


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('surname', 'name', 'post')

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('surname', 'name')
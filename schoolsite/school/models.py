from django.db import models

# Create your models here.

class Teacher(models.Model):
    surname = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255)
    post = models.CharField(max_length=255)
    academic_degree = models.CharField(max_length=255)
    #photo = models.ImageField

    def __str__(self):
        return self.surname

class Student(models.Model):
    surname = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255)
    #number = models.Ph
    #class_number = models.IntegerField()

    def __str__(self):
        return self.surname
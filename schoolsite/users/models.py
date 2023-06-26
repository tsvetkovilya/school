from datetime import datetime

from django.db import models
from django.conf import settings
from school.models import Teacher, CustomUser

class Course(models.Model):

    name = models.CharField(max_length=200, verbose_name='Название предмета')
    description = models.TextField(verbose_name='Описание предмета')
    course_program = models.FileField(upload_to='course_programs/', verbose_name='Ссылка на программу курса')

    def is_registered(self, student):
        return self.registrations.filter(student=student).exists()

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'school'
        verbose_name_plural = 'Курсы'

class CourseRegistration(models.Model):

    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Студент')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')
    # teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Учитель', default=None)
    additional_information = models.CharField(max_length=1000, verbose_name='Дополнительная информация для студента', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        existing_registration = CourseRegistration.objects.filter(student=self.student.id, course=self.course.id)
        if existing_registration.exists():
#           existing_registration.update(teacher=self.teacher, additional_information=self.additional_information)
            existing_registration.update(additional_information=self.additional_information)
            return existing_registration.first()
        else:
            super().save(*args, **kwargs)

    class Meta:
        app_label = 'school'
        verbose_name_plural = 'Регистрация на курс и доп.информация по курсу'
    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} - {self.course.name} "

class Lesson(models.Model):
    # MONDAY = '1'
    # TUESDAY = '2'
    # WEDNESDAY = '3'
    # THURSDAY = '4'
    # FRIDAY = '5'
    # SATURDAY = '6'
    # SUNDAY = '7'
    # DAY_CHOICES = (
    #     (MONDAY, 'Понедельник'),
    #     (TUESDAY, 'Вторник'),
    #     (WEDNESDAY, 'Среда'),
    #     (THURSDAY, 'Четверг'),
    #     (FRIDAY, 'Пятница'),
    #     (SATURDAY, 'Суббота'),
    #     (SUNDAY, 'Воскресенье'),
    # )
    start_time = models.TimeField(verbose_name='Начало урока')
    end_time = models.TimeField(verbose_name='Конец урока')
    day_of_week = models.DateField(verbose_name='Дата')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Учитель')
    lesson_topic = models.CharField(max_length=200, verbose_name='Тема занятия')
    students = models.ManyToManyField(CourseRegistration,  verbose_name='Слушатели')

    class Meta:
        app_label = 'school'
        verbose_name_plural = 'Расписание занятий'
    def __str__(self):
        return  f"{self.course.name} - {self.teacher} - {self.day_of_week}"

class Attendance_of_classes(models.Model):
    lesson = models.ForeignKey(Lesson,  on_delete=models.CASCADE, verbose_name='Курс')
    students = models.ManyToManyField(CourseRegistration, verbose_name='Слушатели')

    class Meta:
        app_label = 'school'
        verbose_name_plural = 'Посещения занятий'
    def __str__(self):
        return  f"{self.lesson.course.name} - {self.lesson.teacher} - {self.lesson.day_of_week}"

class Attendance(models.Model):
    attendance = models.ForeignKey(Attendance_of_classes, on_delete=models.CASCADE, verbose_name='Занятие')
    student = models.ForeignKey(CustomUser, limit_choices_to={'is_staff': False}, on_delete=models.CASCADE, verbose_name='Слушатель')
    grade = models.CharField(max_length=3, null=True, blank=True, verbose_name='Оценка')

    class Meta:
        app_label = 'school'
        verbose_name_plural = 'Оценки слушателей'
    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} - {self.attendance.lesson.course.name} -  {self.grade}"

class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def reset(self):
        self.value = 0

    def get_count(self):
        return self.value

    def weekday(self, date_string):
        date = datetime.strptime(date_string, "%Y-%m-%d")
        is_saturday = date.weekday() == 5
        saturday = 5
        is_sunday = date.weekday() == 6
        sunday = 6

        if is_saturday:
            return self.saturday
        if is_sunday:
            return self.sunday

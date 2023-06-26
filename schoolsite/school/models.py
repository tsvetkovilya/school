from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, Permission, Group, AbstractUser



class Teacher(models.Model):
    mathematics = '1'
    physics = '2'
    computer_science = '3'
    lessons = (
        (mathematics, 'Математика'),
        (physics, 'Физика'),
        (computer_science, 'Информатика и ИКТ'),
    )
    # teacher_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Курс')
    # surname = models.CharField(max_length=255, verbose_name='Фамилия')
    # name = models.CharField(max_length=255, verbose_name='Имя')
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, limit_choices_to={'is_staff': True}, on_delete=models.CASCADE, verbose_name='Преподаватель')
    patronymic = models.CharField(max_length=255, verbose_name='Отчество')
    post = models.CharField(max_length=255, verbose_name='Должность')
    academic_degree = models.CharField(max_length=255, verbose_name='Академическая степень')
    photo = models.CharField(max_length=255, verbose_name='Ссылка на фото')
    additionally = models.CharField(max_length=255, verbose_name='Информация о преподавателе')
    teacher_lesson = models.CharField(max_length=255, choices=lessons, verbose_name='Ведет предмет')

    # user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Добавил пользователь', on_delete=models.CASCADE)

    def __str__(self):
        lesson_name = dict(self.lessons).get(self.teacher_lesson)
        return f"{self.teacher.last_name} {self.teacher.first_name} {self.patronymic} - {lesson_name}"

    class Meta:
        verbose_name_plural = 'Преподаватели'

class School(models.Model):
    address = models.CharField(max_length=255, verbose_name='Адрес школы')
    site = models.CharField(max_length=255, verbose_name='Сайт учебного заведения')
    vk = models.CharField(max_length=255, verbose_name='Ссылка на ВК')
    youtube = models.CharField(max_length=255, verbose_name='Ссылка на YouTube')
    telegram = models.CharField(max_length=255, verbose_name='Ссылка на Telegram')
    email = models.CharField(max_length=255, verbose_name='Email')
    phone_number = models.CharField(max_length=255, verbose_name='Номер телефона школы')
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Добавил пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name_plural = 'Школа'

class CustomUser(AbstractUser):
    wishes = models.CharField(max_length=255, verbose_name='Пожелания к обучению')
    phone_number = models.CharField(max_length=255, verbose_name='Номер телефона')
    grade_number = (
        ('9 класс', '9 класс'),
        ('11 класс', '11 класс'),
        ('Другое', 'Другое')
    )
    grade = models.CharField(max_length=20, choices=grade_number, verbose_name='Класс')
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_users_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    groups = models.ManyToManyField(
        Group,
        related_name='custom_users',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )

    def __str__(self):
        return self.first_name + ' ' + self.last_name
        # return self.username


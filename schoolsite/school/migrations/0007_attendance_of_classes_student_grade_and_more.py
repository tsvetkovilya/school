# Generated by Django 4.1.7 on 2023-06-08 00:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_alter_attendance_of_classes_lesson_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance_of_classes',
            name='student_grade',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='Оценка'),
        ),
        migrations.AlterField(
            model_name='attendance_of_classes',
            name='students',
            field=models.ManyToManyField(limit_choices_to={'is_staff': False}, to=settings.AUTH_USER_MODEL, verbose_name='Слушатели'),
        ),
    ]

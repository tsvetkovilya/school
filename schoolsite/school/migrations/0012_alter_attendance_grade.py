# Generated by Django 4.1.7 on 2023-06-08 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0011_remove_attendance_of_classes_grade_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='grade',
            field=models.IntegerField(blank=True, null=True, verbose_name='Оценка'),
        ),
    ]

# Generated by Django 4.1.7 on 2023-05-29 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseregistration',
            name='additional_information',
            field=models.CharField(blank=True, max_length=1000, verbose_name='Дополнительная информация для студента'),
        ),
    ]

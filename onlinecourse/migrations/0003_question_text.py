# Generated by Django 3.1.3 on 2023-04-11 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_question_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='text',
            field=models.CharField(default='question text', max_length=550),
        ),
    ]
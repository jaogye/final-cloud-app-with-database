# Generated by Django 3.1.3 on 2023-04-11 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0003_question_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='question_text',
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.CharField(default='input a question', max_length=300),
        ),
    ]

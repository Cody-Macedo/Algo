# Generated by Django 3.1.4 on 2020-12-02 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toDoList', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='content',
            field=models.CharField(default='NaN', max_length=255),
        ),
    ]

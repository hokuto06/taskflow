# Generated by Django 4.1.12 on 2023-12-03 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskslist',
            name='owner',
        ),
        migrations.DeleteModel(
            name='SubTask',
        ),
        migrations.DeleteModel(
            name='TasksList',
        ),
    ]

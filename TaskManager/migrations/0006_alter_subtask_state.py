# Generated by Django 4.1.12 on 2023-12-28 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskManager', '0005_subtask_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtask',
            name='state',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
# Generated by Django 2.1.15 on 2020-04-29 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0008_auto_20200429_1956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='subtasks',
        ),
        migrations.AddField(
            model_name='subtask',
            name='task',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='taskmanager.Task', verbose_name='Parent'),
        ),
    ]
# Generated by Django 2.1.15 on 2020-04-27 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0003_auto_20200427_0746'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='comments',
            field=models.ManyToManyField(related_name='Commentaires', to='taskmanager.Comment'),
        ),
    ]

# Generated by Django 2.1.15 on 2020-05-08 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0017_auto_20200508_0903'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trace',
            old_name='objet_project',
            new_name='object_project',
        ),
        migrations.RenameField(
            model_name='trace',
            old_name='objet_tache',
            new_name='object_tache',
        ),
        migrations.RenameField(
            model_name='trace',
            old_name='verbe',
            new_name='verb',
        ),
    ]

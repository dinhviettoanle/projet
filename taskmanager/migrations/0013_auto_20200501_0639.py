# Generated by Django 2.1.15 on 2020-05-01 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0012_project_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='public',
            field=models.CharField(choices=[('PU', 'Public'), ('PR', 'Privé')], default='0', max_length=2, verbose_name='Partage'),
        ),
    ]

# Generated by Django 2.1.15 on 2020-05-01 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0011_auto_20200430_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='public',
            field=models.CharField(choices=[('1', 'Public'), ('0', 'Privé')], default='0', max_length=1, verbose_name='Partage'),
        ),
    ]

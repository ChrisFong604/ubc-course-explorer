# Generated by Django 3.1.1 on 2021-01-03 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coursetracker', '0010_auto_20210102_1054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='prerequisites',
        ),
        migrations.RemoveField(
            model_name='course',
            name='professors_info',
        ),
    ]

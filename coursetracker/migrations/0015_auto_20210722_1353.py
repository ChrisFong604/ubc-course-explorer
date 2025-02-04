# Generated by Django 3.1.13 on 2021-07-22 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursetracker', '0014_remove_course_average'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='average',
            field=models.CharField(default='err', max_length=20),
        ),
        migrations.AlterField(
            model_name='course',
            name='corequisites',
            field=models.TextField(default='err'),
        ),
        migrations.AlterField(
            model_name='course',
            name='corequisites_description',
            field=models.TextField(default='err'),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_description',
            field=models.TextField(default='err'),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_link',
            field=models.TextField(default='err'),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_name',
            field=models.CharField(default='err', max_length=10),
        ),
        migrations.AlterField(
            model_name='course',
            name='dependencies',
            field=models.TextField(default='err'),
        ),
        migrations.AlterField(
            model_name='course',
            name='distribution',
            field=models.TextField(default='err'),
        ),
        migrations.AlterField(
            model_name='course',
            name='distribution_term',
            field=models.CharField(default='err', max_length=5),
        ),
        migrations.AlterField(
            model_name='course',
            name='five_year_average',
            field=models.CharField(default='err', max_length=20),
        ),
        migrations.AlterField(
            model_name='course',
            name='highest_average',
            field=models.CharField(default='err', max_length=20),
        ),
        migrations.AlterField(
            model_name='course',
            name='lowest_average',
            field=models.CharField(default='err', max_length=20),
        ),
        migrations.AlterField(
            model_name='course',
            name='number_of_credits',
            field=models.CharField(default='err', max_length=5),
        ),
        migrations.AlterField(
            model_name='course',
            name='prerequistes_description',
            field=models.TextField(default='err'),
        ),
        migrations.AlterField(
            model_name='course',
            name='standard_deviation',
            field=models.CharField(default='err', max_length=20),
        ),
        migrations.AlterField(
            model_name='course',
            name='sub_name',
            field=models.CharField(default='err', max_length=100),
        ),
    ]

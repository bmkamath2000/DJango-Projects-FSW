# Generated by Django 5.0.6 on 2024-06-27 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enrollmentapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='students',
        ),
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(to='enrollmentapp.course'),
        ),
    ]

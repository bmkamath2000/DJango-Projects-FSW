# Generated by Django 5.0.6 on 2024-06-12 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTableComment(
            name='course',
            table_comment=None,
        ),
        migrations.AlterModelTableComment(
            name='student',
            table_comment=None,
        ),
        migrations.RemoveField(
            model_name='student',
            name='course',
        ),
    ]
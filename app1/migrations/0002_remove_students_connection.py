# Generated by Django 5.0.1 on 2024-03-06 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='connection',
        ),
    ]

# Generated by Django 3.0.7 on 2022-04-16 02:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_enroll'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Enroll',
            new_name='Enrollment',
        ),
    ]
# Generated by Django 3.0.7 on 2022-04-24 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_auto_20220415_2334'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='cellphone',
            field=models.CharField(default='', max_length=11),
        ),
    ]
# Generated by Django 3.1.3 on 2020-12-15 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('standart', '0042_auto_20201215_1224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='container',
            name='subname',
        ),
        migrations.RemoveField(
            model_name='examples',
            name='subname',
        ),
    ]

# Generated by Django 3.1.3 on 2020-12-02 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('standart', '0025_navconstruct_example'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='navconstruct',
            name='example',
        ),
    ]

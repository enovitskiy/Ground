# Generated by Django 3.1.3 on 2020-12-28 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('standart', '0054_auto_20201222_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navconstruct',
            name='example',
            field=models.TextField(blank=True, help_text='наличие иконки в navbar', null=True, verbose_name='Иконка'),
        ),
    ]

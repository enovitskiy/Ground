# Generated by Django 3.1.3 on 2020-12-02 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('standart', '0026_remove_navconstruct_example'),
    ]

    operations = [
        migrations.AddField(
            model_name='navconstruct',
            name='example',
            field=models.BooleanField(default=False, help_text='наличие примеров в разделе', verbose_name='Наличие примера'),
        ),
    ]

# Generated by Django 3.1.3 on 2020-12-02 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('standart', '0024_examplestranslation_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='navconstruct',
            name='example',
            field=models.CharField(blank=True, help_text='наличие примеров в разделе', max_length=30, null=True, unique=True, verbose_name='Наличие примера'),
        ),
    ]

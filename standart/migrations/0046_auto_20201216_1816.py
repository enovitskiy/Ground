# Generated by Django 3.1.3 on 2020-12-16 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('standart', '0045_auto_20201216_1752'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='metka',
            options={'ordering': ['translations__title'], 'verbose_name': 'Категория проекта', 'verbose_name_plural': 'Категории проектов'},
        ),
        migrations.AlterModelOptions(
            name='metkatranslation',
            options={'default_permissions': (), 'managed': True, 'verbose_name': 'Категория проекта Translation'},
        ),
        migrations.AlterField(
            model_name='navconstructtranslation',
            name='alt',
            field=models.TextField(blank=True, help_text='текст блока', max_length=300, verbose_name='Текст блока'),
        ),
        migrations.AlterField(
            model_name='navconstructtranslation',
            name='hreflogo',
            field=models.CharField(blank=True, help_text='текст блока', max_length=100, verbose_name='Текст блока'),
        ),
        migrations.AlterField(
            model_name='navconstructtranslation',
            name='title',
            field=models.TextField(blank=True, help_text='описание заголовка в строке браузера', max_length=300, verbose_name='Заголовок'),
        ),
    ]
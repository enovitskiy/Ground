# Generated by Django 3.1.3 on 2020-11-21 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('standart', '0009_auto_20201121_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='container',
            field=models.ForeignKey(blank=True, help_text='привязка к Templates', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='container', to='standart.container', verbose_name='Templates'),
        ),
        migrations.AlterField(
            model_name='container',
            name='template_name',
            field=models.ForeignKey(blank=True, help_text='привязка к Templates', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='template', to='standart.templates', verbose_name='Templates'),
        ),
    ]
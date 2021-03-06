# Generated by Django 3.1.3 on 2020-11-25 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('standart', '0015_auto_20201121_2337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='navconstructtranslation',
            name='template_name',
        ),
        migrations.RemoveField(
            model_name='pictures',
            name='image',
        ),
        migrations.RemoveField(
            model_name='subnavigatortranslation',
            name='template_name',
        ),
        migrations.AddField(
            model_name='navconstruct',
            name='template_name',
            field=models.ForeignKey(blank=True, help_text='привязка к Templates', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='navtemp', to='standart.templates', verbose_name='Templates'),
        ),
        migrations.AddField(
            model_name='subnavigator',
            name='template_name',
            field=models.ForeignKey(blank=True, help_text='привязка к Templates', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subtemp', to='standart.templates', verbose_name='Templates'),
        ),
        migrations.AlterField(
            model_name='picturestranslation',
            name='alt',
            field=models.CharField(help_text='название основного раздела', max_length=200, verbose_name='Название раздела'),
        ),
        migrations.AlterField(
            model_name='text',
            name='pictures',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='picture', to='standart.pictures'),
        ),
    ]

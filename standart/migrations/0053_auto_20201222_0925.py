# Generated by Django 3.1.3 on 2020-12-22 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('standart', '0052_auto_20201222_0923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorytranslation',
            name='slug',
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
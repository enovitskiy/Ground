# Generated by Django 3.1.3 on 2020-12-02 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('standart', '0022_auto_20201202_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examples',
            name='marks',
            field=models.ManyToManyField(blank=True, related_name='marks', to='standart.Metka'),
        ),
    ]

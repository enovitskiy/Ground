# Generated by Django 3.1.3 on 2020-12-03 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('standart', '0034_templates_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='navconstruct',
            name='pictures',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='navpict', to='standart.pictures'),
        ),
    ]

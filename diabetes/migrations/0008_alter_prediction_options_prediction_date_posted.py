# Generated by Django 4.0.3 on 2022-08-05 17:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('diabetes', '0007_carausel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prediction',
            options={'verbose_name': 'Report', 'verbose_name_plural': 'Reports'},
        ),
        migrations.AddField(
            model_name='prediction',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

# Generated by Django 4.1 on 2022-08-15 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diabetes', '0009_alter_prediction_age_alter_prediction_blood_pressure_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prediction',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

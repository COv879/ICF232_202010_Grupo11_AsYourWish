# Generated by Django 3.1.1 on 2020-10-24 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base_Alumno', '0003_auto_20201023_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagosalumno',
            name='id_Alumno',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.1.1 on 2020-10-22 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Local', models.CharField(max_length=35)),
                ('Anno', models.IntegerField()),
                ('Mes', models.CharField(max_length=11)),
                ('NombreLocal', models.CharField(max_length=20)),
                ('PromedioIngresos', models.IntegerField()),
                ('TasaAsist', models.IntegerField()),
                ('TotalAlumnos', models.IntegerField()),
                ('NuevosAlumnos', models.IntegerField()),
            ],
        ),
    ]

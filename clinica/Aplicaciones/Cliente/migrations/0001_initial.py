# Generated by Django 3.1.3 on 2023-11-05 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('codigo', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('sexo', models.CharField(max_length=10)),
            ],
        ),
    ]

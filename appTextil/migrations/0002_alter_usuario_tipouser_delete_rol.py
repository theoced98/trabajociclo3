# Generated by Django 4.1 on 2022-09-29 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appTextil', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='tipouser',
            field=models.CharField(choices=[('E', 'Empleado'), ('V', 'Visitante')], default='V', max_length=1),
        ),
        migrations.DeleteModel(
            name='rol',
        ),
    ]
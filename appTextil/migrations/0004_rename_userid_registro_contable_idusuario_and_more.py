# Generated by Django 4.1 on 2022-09-30 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appTextil', '0003_registro_contable_userid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registro_contable',
            old_name='userid',
            new_name='idusuario',
        ),
        migrations.AlterField(
            model_name='empresa',
            name='nit',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]

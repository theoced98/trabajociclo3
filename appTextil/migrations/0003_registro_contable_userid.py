# Generated by Django 4.1 on 2022-09-30 00:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appTextil', '0002_alter_usuario_tipouser_delete_rol'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro_contable',
            name='userid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appTextil.usuario'),
        ),
    ]
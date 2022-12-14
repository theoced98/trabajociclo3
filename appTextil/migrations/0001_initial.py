# Generated by Django 4.1 on 2022-09-29 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='empresa',
            fields=[
                ('empresa_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=50)),
                ('nit', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='rol',
            fields=[
                ('rol_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('tipo', models.CharField(choices=[('E', 'Empleado'), ('V', 'Visitante')], default='V', max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('user_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=50)),
                ('tipouser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appTextil.rol')),
            ],
        ),
        migrations.CreateModel(
            name='registro_contable',
            fields=[
                ('idregis', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('fecha', models.DateField(auto_now=True)),
                ('tipo', models.CharField(choices=[('I', 'Ingreso'), ('E', 'Egreso')], default='I', max_length=1)),
                ('valor', models.IntegerField(null=True)),
                ('empresa_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appTextil.empresa')),
            ],
        ),
        migrations.CreateModel(
            name='empleado',
            fields=[
                ('empleado_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('empresa_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appTextil.empresa')),
                ('registro_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appTextil.registro_contable')),
                ('usuario_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appTextil.usuario')),
            ],
        ),
    ]

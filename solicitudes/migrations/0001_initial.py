# Generated by Django 2.2.5 on 2019-10-17 00:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aplicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('link', models.TextField(blank=True, null=True)),
                ('version', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('creado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Herramienta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('link', models.TextField(blank=True, null=True)),
                ('version', models.CharField(max_length=100)),
                ('alto_pantalla', models.IntegerField(default=600)),
                ('ancho_pantalla', models.IntegerField(default=800)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('creado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Prueba',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('script', models.TextField(blank=True, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('creado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('herramienta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='solicitudes.Herramienta')),
            ],
        ),
        migrations.CreateModel(
            name='TipoAplicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_aplicacion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TipoPrueba',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_prueba', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TipoEjecucion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_ejecucion', models.CharField(max_length=100)),
                ('tipo_prueba', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='solicitudes.TipoPrueba')),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('aplicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='solicitudes.Aplicacion')),
                ('creado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('herramienta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='solicitudes.Herramienta')),
                ('pruebas', models.ManyToManyField(to='solicitudes.Prueba')),
                ('tipo_ejecucion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='solicitudes.TipoEjecucion')),
                ('tipo_prueba', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='solicitudes.TipoPrueba')),
            ],
        ),
        migrations.AddField(
            model_name='prueba',
            name='tipo_prueba',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='solicitudes.TipoPrueba'),
        ),
        migrations.AddField(
            model_name='herramienta',
            name='tipo_aplicacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='solicitudes.TipoAplicacion'),
        ),
        migrations.AddField(
            model_name='aplicacion',
            name='tipo_aplicacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='solicitudes.TipoAplicacion'),
        ),
    ]

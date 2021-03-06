# Generated by Django 2.2.5 on 2019-11-07 20:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0007_auto_20191101_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aplicacion',
            name='creado_por',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aplicaciones', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='aplicacion',
            name='tipo_aplicacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aplicaciones', to='solicitudes.TipoAplicacion'),
        ),
        migrations.AlterField(
            model_name='herramienta',
            name='creado_por',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='herramientas', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='herramienta',
            name='ejecutor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='herramientas', to='solicitudes.Ejecutor'),
        ),
        migrations.AlterField(
            model_name='herramienta',
            name='tipo_aplicacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='herramientas', to='solicitudes.TipoAplicacion'),
        ),
        migrations.AlterField(
            model_name='prueba',
            name='aplicacion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pruebas', to='solicitudes.Aplicacion'),
        ),
        migrations.AlterField(
            model_name='prueba',
            name='creado_por',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pruebas', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='prueba',
            name='tipo_prueba',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pruebas', to='solicitudes.TipoPrueba'),
        ),
        migrations.RemoveField(
            model_name='solicitud',
            name='aplicacion',
        ),
        migrations.AddField(
            model_name='solicitud',
            name='aplicacion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='solicitudes', to='solicitudes.Aplicacion'),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='creado_por',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solicitudes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='solicitud',
            name='herramienta',
        ),
        migrations.AddField(
            model_name='solicitud',
            name='herramienta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='solicitudes', to='solicitudes.Herramienta'),
        ),
        migrations.RemoveField(
            model_name='solicitud',
            name='pruebas',
        ),
        migrations.AddField(
            model_name='solicitud',
            name='pruebas',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='solicitudes', to='solicitudes.Prueba'),
        ),
        migrations.RemoveField(
            model_name='solicitud',
            name='tipo_ejecucion',
        ),
        migrations.AddField(
            model_name='solicitud',
            name='tipo_ejecucion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='solicitudes', to='solicitudes.TipoEjecucion'),
        ),
        migrations.RemoveField(
            model_name='solicitud',
            name='tipo_prueba',
        ),
        migrations.AddField(
            model_name='solicitud',
            name='tipo_prueba',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='solicitudes', to='solicitudes.TipoPrueba'),
        ),
        migrations.AlterField(
            model_name='tipoejecucion',
            name='tipo_prueba',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tipos_ejecuciones', to='solicitudes.TipoPrueba'),
        ),
    ]

# Generated by Django 2.2.5 on 2019-10-17 03:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0003_remove_prueba_herramienta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ejecutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ejecutor', models.CharField(max_length=100)),
                ('version', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='herramienta',
            name='version',
        ),
        migrations.AddField(
            model_name='herramienta',
            name='ejecutor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='solicitudes.Ejecutor'),
        ),
    ]

# Generated by Django 3.1 on 2020-09-13 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cuenta', '0002_auto_20200913_1344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil_trabajador',
            name='titulo',
        ),
        migrations.RemoveField(
            model_name='titulo',
            name='matricula',
        ),
        migrations.CreateModel(
            name='Matricula_Titulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(max_length=30, null=True)),
                ('titulo', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='titulo_matricula', to='cuenta.titulo')),
                ('trabajador', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='trabajandor_matricula', to='cuenta.perfil_trabajador')),
            ],
        ),
    ]

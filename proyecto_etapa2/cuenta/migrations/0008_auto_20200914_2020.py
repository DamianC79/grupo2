# Generated by Django 3.1.1 on 2020-09-14 23:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cuenta', '0007_auto_20200914_1820'),
    ]

    operations = [
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciudad', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_pro', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='perfil',
            name='localidad',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='personas_por_ciudad', to='cuenta.localidad'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='provincia',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='personas_por_provincia', to='cuenta.provincia'),
        ),
    ]
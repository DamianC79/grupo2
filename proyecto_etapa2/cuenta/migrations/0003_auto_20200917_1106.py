# Generated by Django 3.1.1 on 2020-09-17 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuenta', '0002_auto_20200917_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='experiencia_laboral',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
# Generated by Django 3.2.8 on 2021-11-21 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0018_alter_comentario_padre'),
    ]

    operations = [
        migrations.AddField(
            model_name='historialcertamen',
            name='n_correctas',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='historialcertamen',
            name='n_preguntas',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='historialcertamen',
            name='puntos',
            field=models.IntegerField(default=0),
        ),
    ]
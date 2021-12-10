# Generated by Django 3.2.8 on 2021-11-07 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0003_auto_20211107_1214'),
    ]

    operations = [
        migrations.RenameField(
            model_name='preguntasmate',
            old_name='solucion',
            new_name='posible_desarrollo',
        ),
        migrations.RenameField(
            model_name='preguntasmate',
            old_name='contenido',
            new_name='tema',
        ),
        migrations.AddField(
            model_name='preguntasmate',
            name='alternativa_a',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='preguntasmate',
            name='alternativa_b',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='preguntasmate',
            name='alternativa_c',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='preguntasmate',
            name='alternativa_d',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='preguntasmate',
            name='alternativa_e',
            field=models.TextField(null=True),
        ),
    ]

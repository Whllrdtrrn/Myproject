# Generated by Django 4.1.1 on 2022-09-15 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaccimo', '0002_sideeffect'),
    ]

    operations = [
        migrations.AddField(
            model_name='sideeffect',
            name='chills',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sideeffect',
            name='fatigue',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sideeffect',
            name='fever',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sideeffect',
            name='feverish',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sideeffect',
            name='headache',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sideeffect',
            name='induration',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sideeffect',
            name='itch',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sideeffect',
            name='join_pain',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sideeffect',
            name='muscle_ache',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sideeffect',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sideeffect',
            name='nausea',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sideeffect',
            name='redness',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sideeffect',
            name='swelling',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sideeffect',
            name='tenderness',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sideeffect',
            name='vomiting',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sideeffect',
            name='warmth',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterModelTable(
            name='sideeffect',
            table='Sideeffect',
        ),
    ]

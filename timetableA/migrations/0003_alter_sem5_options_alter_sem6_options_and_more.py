# Generated by Django 4.0.4 on 2022-04-27 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetableA', '0002_sem5'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sem5',
            options={'verbose_name': 'Sem5', 'verbose_name_plural': 'Sem5'},
        ),
        migrations.AlterModelOptions(
            name='sem6',
            options={'verbose_name': 'Sem6', 'verbose_name_plural': 'Sem6'},
        ),
        migrations.AlterField(
            model_name='sem5',
            name='time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='sem6',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]

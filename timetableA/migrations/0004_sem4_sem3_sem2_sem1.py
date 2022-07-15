# Generated by Django 4.0.4 on 2022-04-27 01:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('timetableA', '0003_alter_sem5_options_alter_sem6_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sem4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Program', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('date', models.DateField(null=True)),
                ('time', models.TimeField(null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Sem4',
                'verbose_name_plural': 'Sem4',
            },
        ),
        migrations.CreateModel(
            name='Sem3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Program', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('date', models.DateField(null=True)),
                ('time', models.TimeField(null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Sem3',
                'verbose_name_plural': 'Sem3',
            },
        ),
        migrations.CreateModel(
            name='Sem2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Program', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('date', models.DateField(null=True)),
                ('time', models.TimeField(null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Sem2',
                'verbose_name_plural': 'Sem2',
            },
        ),
        migrations.CreateModel(
            name='Sem1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Program', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('date', models.DateField(null=True)),
                ('time', models.TimeField(null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Sem1',
                'verbose_name_plural': 'Sem1',
            },
        ),
    ]
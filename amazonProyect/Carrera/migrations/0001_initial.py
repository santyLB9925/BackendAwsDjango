# Generated by Django 2.2.1 on 2019-11-28 18:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=254)),
                ('delete', models.BooleanField(default=False)),
                ('create', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'Carrera',
            },
        ),
    ]

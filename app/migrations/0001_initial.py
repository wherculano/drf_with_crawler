# Generated by Django 3.2.9 on 2021-11-11 16:43

import jsonfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=200)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('hdd', jsonfield.fields.JSONField()),
                ('avaliacoes', models.IntegerField()),
                ('nota', models.IntegerField()),
            ],
        ),
    ]
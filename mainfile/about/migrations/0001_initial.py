# Generated by Django 5.0.3 on 2024-03-30 14:07

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='about_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_des', tinymce.models.HTMLField()),
                ('experience', models.IntegerField()),
                ('chefc', models.IntegerField()),
            ],
        ),
    ]
# Generated by Django 4.2 on 2023-04-28 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soocalendar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=80),
        ),
    ]
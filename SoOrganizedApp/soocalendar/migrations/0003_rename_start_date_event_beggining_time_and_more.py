# Generated by Django 4.2 on 2023-04-29 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('soocalendar', '0002_alter_event_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='start_date',
            new_name='beggining_time',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='end_date',
            new_name='end_time',
        ),
    ]
# Generated by Django 3.2.5 on 2021-08-04 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_rename_timetosend_tasks_time_to_send'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='location',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='designation',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='phone_number',
        ),
    ]

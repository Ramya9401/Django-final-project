# Generated by Django 3.0 on 2021-07-24 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0003_medic_pid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medic',
            name='pid',
        ),
    ]
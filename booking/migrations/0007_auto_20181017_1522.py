# Generated by Django 2.1.1 on 2020-10-25 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_remove_guestdetails_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='room_type',
            field=models.CharField(choices=[('Single-AC', 'Single-AC'), ('Double-AC', 'Double-AC'), ('Single-NON-AC', 'Single NON-AC'), ('Double-NON-AC', 'Double-NON-AC')], max_length=20),
        ),
    ]

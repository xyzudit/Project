# Generated by Django 4.2.11 on 2024-03-16 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0009_remove_attendance_latitude_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
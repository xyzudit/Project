# Generated by Django 4.2.11 on 2024-03-15 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0003_alter_attendance_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='location_image',
            field=models.ImageField(blank=True, null=True, upload_to='attendance_location_images/'),
        ),
    ]
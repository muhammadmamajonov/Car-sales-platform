# Generated by Django 4.2.2 on 2023-09-07 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0005_rename_length_sizeandspace_length_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maintenancemanagementadvantagestranslation',
            old_name='title',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='safetyandconvenienceadvantagestranslation',
            old_name='title',
            new_name='text',
        ),
    ]

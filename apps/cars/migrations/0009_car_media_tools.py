# Generated by Django 4.2.2 on 2023-10-09 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specifications', '0003_externalbodykit_mediatools_optics_salon_and_more'),
        ('cars', '0008_car_number_of_owners'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='media_tools',
            field=models.ManyToManyField(related_name='cars', to='specifications.mediatools'),
        ),
    ]

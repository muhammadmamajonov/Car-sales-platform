# Generated by Django 4.2.2 on 2023-06-26 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_car_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='owned_by_orient_motors',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='car',
            name='rate',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='car',
            name='currency',
            field=models.CharField(choices=[('Usd', 'usd'), ('Uzs', 'uzs')], help_text='usd/uzs', max_length=4),
        ),
    ]

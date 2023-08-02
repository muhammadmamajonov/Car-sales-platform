# Generated by Django 4.2.2 on 2023-08-02 12:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('specifications', '0001_initial'),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('icon', models.URLField()),
                ('used', models.PositiveIntegerField(default=0)),
            ],
            options={
                'db_table': 'brand',
            },
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('used', models.PositiveIntegerField(default=0)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.brand')),
            ],
            options={
                'db_table': 'car_model',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveSmallIntegerField(help_text='Ishlab chiqarilgan yil')),
                ('month', models.PositiveSmallIntegerField(blank=True, help_text='Ishlab chiqarilgan oy', null=True)),
                ('mileage', models.PositiveIntegerField(default=0)),
                ('price', models.PositiveBigIntegerField()),
                ('currency', models.CharField(choices=[('Usd', 'usd'), ('Uzs', 'uzs')], help_text='usd/uzs', max_length=4)),
                ('engine_size', models.FloatField(default=0)),
                ('horsepower', models.PositiveSmallIntegerField()),
                ('used_car', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('rate', models.PositiveSmallIntegerField(default=0)),
                ('owned_by_orient_motors', models.BooleanField(default=False)),
                ('avtoritet_diagnostics', models.BooleanField()),
                ('avtoritet_premium_diagnostics', models.BooleanField()),
                ('orient_motors_warranty', models.BooleanField()),
                ('body_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='specifications.bodytype')),
                ('color', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='specifications.color')),
                ('fuel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='specifications.fuel')),
                ('liked_by', models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL)),
                ('model', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cars.model')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.region')),
                ('transmission', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='specifications.transmission')),
            ],
            options={
                'db_table': 'car',
            },
        ),
    ]

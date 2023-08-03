# Generated by Django 4.2.2 on 2023-08-03 09:35

from django.db import migrations, models
import django.db.models.deletion
import parler.fields
import parler.models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_alter_diagnosticspecialiststranslation_specialty'),
    ]

    operations = [
        migrations.CreateModel(
            name='PremiumDiagnosticsHeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='premium_dagnostics/header-video')),
            ],
            options={
                'abstract': False,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PremiumDiagnosticsHeaderTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('text', models.TextField()),
                ('sub_text', models.TextField()),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='services.premiumdiagnosticsheader')),
            ],
            options={
                'verbose_name': 'premium diagnostics header Translation',
                'db_table': 'services_premiumdiagnosticsheader_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]
# Generated by Django 4.2.2 on 2023-08-23 05:19

from django.db import migrations, models
import django.db.models.deletion
import parler.fields
import parler.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='car-review')),
            ],
            options={
                'db_table': 'review',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CarReviewFAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faq', to='review.carreview')),
            ],
            options={
                'db_table': 'car_review_faq',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Design',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rated_by_orient_motors', models.PositiveSmallIntegerField(default=0)),
                ('photo', models.ImageField(upload_to='car-review/design')),
                ('car_review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='design', to='review.carreview')),
            ],
            options={
                'db_table': 'review_design',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='MaintenanceAndManagement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rated_by_orient_motors', models.PositiveSmallIntegerField(default=0)),
                ('photo', models.ImageField(upload_to='car-review/maintenance_management')),
                ('car_review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maintenance_management', to='review.carreview')),
            ],
            options={
                'db_table': 'review_maintenance_management',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='MaintenanceManagementAdvantages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maintenance_management', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='advantages', to='review.maintenanceandmanagement')),
            ],
            options={
                'db_table': 'review_maintenance_management_advantages',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='car-review/performance')),
                ('rated_by_orient_motors', models.PositiveSmallIntegerField(default=0)),
                ('car_review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='performance', to='review.carreview')),
            ],
            options={
                'db_table': 'review_performance',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PerformanceAdvantages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rated', models.PositiveSmallIntegerField(default=0)),
                ('performance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='advantages', to='review.performance')),
            ],
            options={
                'db_table': 'review_performance_advantage',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PerformanceFlaws',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rated', models.PositiveSmallIntegerField(default=0)),
                ('performance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flaws', to='review.performance')),
            ],
            options={
                'db_table': 'review_performance_flaws',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='SizeAndSpace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height_width_photo', models.ImageField(upload_to='car-review/size-space/height-width-photo')),
                ('length', models.ImageField(upload_to='car-review/size-space/length-photo')),
                ('car_review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='size_space', to='review.carreview')),
            ],
            options={
                'db_table': 'review_size_space',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Synthesis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='synthesis', to='review.carreview')),
            ],
            options={
                'db_table': 'synthesis',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='SizeAndSpacePhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='car-review/size-space/photos')),
                ('size_space', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='review.sizeandspace')),
            ],
            options={
                'db_table': 'review_size_space_photo',
            },
        ),
        migrations.CreateModel(
            name='InteriorDesignPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='car-review/design/interior')),
                ('design', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interior_photos', to='review.design')),
            ],
            options={
                'db_table': 'review_interior_disign_photo',
            },
        ),
        migrations.CreateModel(
            name='ExternalDesignPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='car-review/design/external')),
                ('design', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='external_photos', to='review.design')),
            ],
            options={
                'db_table': 'review_external_disign_photo',
            },
        ),
        migrations.CreateModel(
            name='SynthesisTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('text', models.TextField()),
                ('advantage', models.CharField(max_length=200)),
                ('flaw', models.CharField(max_length=200)),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='review.synthesis')),
            ],
            options={
                'verbose_name': 'synthesis Translation',
                'db_table': 'synthesis_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='SizeAndSpaceTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(max_length=100)),
                ('dimensions_and_space', models.TextField()),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='review.sizeandspace')),
            ],
            options={
                'verbose_name': 'size and space Translation',
                'db_table': 'review_size_space_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PerformanceTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(max_length=100)),
                ('direct_driving', models.TextField()),
                ('curved_driving', models.TextField()),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='review.performance')),
            ],
            options={
                'verbose_name': 'performance Translation',
                'db_table': 'review_performance_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PerformanceFlawsTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(max_length=100)),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='review.performanceflaws')),
            ],
            options={
                'verbose_name': 'performance flaws Translation',
                'db_table': 'review_performance_flaws_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PerformanceAdvantagesTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(max_length=100)),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='review.performanceadvantages')),
            ],
            options={
                'verbose_name': 'performance advantages Translation',
                'db_table': 'review_performance_advantage_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='MaintenanceManagementAdvantagesTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(max_length=100)),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='review.maintenancemanagementadvantages')),
            ],
            options={
                'verbose_name': 'maintenance management advantages Translation',
                'db_table': 'review_maintenance_management_advantages_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='MaintenanceAndManagementTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(max_length=200)),
                ('fuel_efficiency', models.TextField()),
                ('Service', models.TextField()),
                ('warranty', models.TextField()),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='review.maintenanceandmanagement')),
            ],
            options={
                'verbose_name': 'maintenance and management Translation',
                'db_table': 'review_maintenance_management_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='DesignTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(max_length=200)),
                ('external_design', models.TextField()),
                ('interior_design', models.TextField()),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='review.design')),
            ],
            options={
                'verbose_name': 'design Translation',
                'db_table': 'review_design_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CarReviewTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=200)),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='review.carreview')),
            ],
            options={
                'verbose_name': 'car review Translation',
                'db_table': 'review_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CarReviewFAQTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('question', models.CharField(max_length=200)),
                ('answer', models.TextField()),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='review.carreviewfaq')),
            ],
            options={
                'verbose_name': 'car review faq Translation',
                'db_table': 'car_review_faq_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]

# Generated by Django 4.1.5 on 2023-01-18 12:59

from django.db import migrations, models
import django.db.models.deletion
import parler.fields
import parler.models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='F.I.O')),
                ('phone', models.CharField(max_length=15, verbose_name='Telefon raqami')),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
            bases=(parler.models.TranslatableModel, models.Model),
        ),
        migrations.CreateModel(
            name='DistrictTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(max_length=255, verbose_name='Tuman nomi')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='landing.district')),
            ],
            options={
                'verbose_name': 'district Translation',
                'db_table': 'landing_district_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatableModel, models.Model),
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
            bases=(parler.models.TranslatableModel, models.Model),
        ),
        migrations.CreateModel(
            name='FAQTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('question', models.CharField(max_length=255, verbose_name='Title')),
                ('answer', models.TextField(verbose_name='Body')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='landing.faq')),
            ],
            options={
                'verbose_name': 'faq Translation',
                'db_table': 'landing_faq_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatableModel, models.Model),
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
            bases=(parler.models.TranslatableModel, models.Model),
        ),
        migrations.CreateModel(
            name='RegionTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(max_length=255, verbose_name='Viloyat nomi')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='landing.region')),
            ],
            options={
                'verbose_name': 'region Translation',
                'db_table': 'landing_region_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatableModel, models.Model),
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('upload', models.ImageField(upload_to='uploads/%Y/%m/%d/')),
                ('created_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Updated At')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_to_category', to='landing.category')),
            ],
            options={
                'abstract': False,
            },
            bases=(parler.models.TranslatableModel, models.Model),
        ),
        migrations.CreateModel(
            name='ServiceTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('meta_d', models.CharField(max_length=255, verbose_name='Meta description')),
                ('meta_k', models.CharField(max_length=255, verbose_name='Meta keywords')),
                ('body', models.TextField(verbose_name='Body')),
                ('short_desc', models.TextField(verbose_name='Short Desc')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='landing.service')),
            ],
            options={
                'verbose_name': 'service Translation',
                'db_table': 'landing_service_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatableModel, models.Model),
        ),
        migrations.AlterUniqueTogether(
            name='servicestranslation',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='servicestranslation',
            name='master',
        ),
        migrations.AlterField(
            model_name='categorytranslation',
            name='body',
            field=models.TextField(verbose_name='Body'),
        ),
        migrations.DeleteModel(
            name='Services',
        ),
        migrations.DeleteModel(
            name='ServicesTranslation',
        ),
        migrations.AddField(
            model_name='faq',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faq_to_service', to='landing.service'),
        ),
        migrations.AddField(
            model_name='district',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='district_to_region', to='landing.region'),
        ),
        migrations.AddField(
            model_name='client',
            name='district',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='client_to_district', to='landing.district'),
        ),
        migrations.AddField(
            model_name='client',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='client_to_region', to='landing.region'),
        ),
    ]

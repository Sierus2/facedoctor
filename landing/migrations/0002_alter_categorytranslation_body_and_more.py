# Generated by Django 4.1.5 on 2023-01-16 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorytranslation',
            name='body',
            field=models.TextField(verbose_name='Body'),
        ),
        migrations.AlterField(
            model_name='servicestranslation',
            name='body',
            field=models.TextField(verbose_name='Body'),
        ),
    ]

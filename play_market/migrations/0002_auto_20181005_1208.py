# Generated by Django 2.1.2 on 2018-10-05 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play_market', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='app',
            name='dev',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='app',
            name='image',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='app',
            name='score',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='app',
            name='title',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='app',
            name='url',
            field=models.TextField(blank=True, null=True),
        ),
    ]
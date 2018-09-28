# Generated by Django 2.1.1 on 2018-09-28 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_id', models.CharField(max_length=300)),
                ('title', models.TextField(blank=True)),
                ('image', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('url', models.TextField(blank=True)),
                ('dev_id', models.CharField(max_length=300)),
                ('dev', models.TextField(blank=True)),
                ('score', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True)),
                ('mnemonic_name', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='app',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='play_market.Category'),
        ),
    ]
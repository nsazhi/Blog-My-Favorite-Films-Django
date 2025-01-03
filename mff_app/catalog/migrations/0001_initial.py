# Generated by Django 4.2.17 on 2025-01-03 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('release', models.IntegerField()),
                ('country', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=100)),
                ('actors', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=300)),
                ('img_url', models.CharField(max_length=200)),
                ('is_viewed', models.BooleanField(default=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.category')),
            ],
        ),
    ]
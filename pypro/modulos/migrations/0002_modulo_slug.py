# Generated by Django 5.0.1 on 2024-01-30 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='modulo',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
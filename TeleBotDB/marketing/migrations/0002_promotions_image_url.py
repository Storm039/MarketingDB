# Generated by Django 4.0.4 on 2022-04-22 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='promotions',
            name='image_url',
            field=models.CharField(blank=True, max_length=255, verbose_name='Image URL'),
        ),
    ]

# Generated by Django 4.0.4 on 2022-04-26 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0002_promotions_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='promotions',
            name='guid_one_c',
            field=models.CharField(default='', max_length=36, unique=True, verbose_name='1C GUID'),
        ),
        migrations.AlterField(
            model_name='promotions',
            name='data_sync',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Sync date with other app'),
        ),
        migrations.AlterField(
            model_name='promotions',
            name='description',
            field=models.TextField(verbose_name='Date end of action'),
        ),
    ]

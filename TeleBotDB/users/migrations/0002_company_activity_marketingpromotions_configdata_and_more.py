# Generated by Django 4.0.4 on 2022-04-22 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='activity',
            field=models.BooleanField(default=True, verbose_name='Аctivity'),
        ),
        migrations.CreateModel(
            name='MarketingPromotions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateTimeField(verbose_name='Date beginning of the action')),
                ('date_end', models.DateTimeField(verbose_name='Date end of action')),
                ('description', models.TextField(blank=True, verbose_name='Date end of action')),
                ('activity', models.BooleanField(default=True, verbose_name='Аctivity')),
                ('data_sync', models.DateTimeField(verbose_name='Sync date with other app')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.company', verbose_name='Company')),
            ],
        ),
        migrations.CreateModel(
            name='ConfigData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('param_key', models.CharField(max_length=200, verbose_name='Param key')),
                ('param_val', models.TextField(blank=True, verbose_name='Date end of action')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.company', verbose_name='Company')),
            ],
        ),
        migrations.CreateModel(
            name='Bonuses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Number of points')),
                ('data_sync', models.DateTimeField(verbose_name='Sync date with other app')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.users', verbose_name='Users')),
            ],
        ),
    ]

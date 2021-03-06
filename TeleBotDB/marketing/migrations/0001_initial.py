# Generated by Django 4.0.4 on 2022-04-22 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0004_remove_configdata_company_and_more'),
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promotions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateTimeField(verbose_name='Date beginning of the action')),
                ('date_end', models.DateTimeField(verbose_name='Date end of action')),
                ('description', models.TextField(blank=True, verbose_name='Date end of action')),
                ('activity', models.BooleanField(default=True, verbose_name='Аctivity')),
                ('data_sync', models.DateTimeField(verbose_name='Sync date with other app')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company', verbose_name='Company')),
            ],
            options={
                'verbose_name': 'Marketing promotion',
                'verbose_name_plural': 'Marketing promotions',
            },
        ),
        migrations.CreateModel(
            name='Bonuses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Number of points')),
                ('data_sync', models.DateTimeField(verbose_name='Sync date with other app')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.users', verbose_name='Users')),
            ],
            options={
                'verbose_name': 'Bonus',
                'verbose_name_plural': 'Bonuses',
            },
        ),
    ]

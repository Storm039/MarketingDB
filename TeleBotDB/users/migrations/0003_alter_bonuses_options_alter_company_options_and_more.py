# Generated by Django 4.0.4 on 2022-04-22 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_company_activity_marketingpromotions_configdata_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bonuses',
            options={'verbose_name': 'Bonus', 'verbose_name_plural': 'Bonuses'},
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': 'Company', 'verbose_name_plural': 'Company'},
        ),
        migrations.AlterModelOptions(
            name='configdata',
            options={'verbose_name': 'Config data', 'verbose_name_plural': 'Config'},
        ),
        migrations.AlterModelOptions(
            name='marketingpromotions',
            options={'verbose_name': 'Marketing promotion', 'verbose_name_plural': 'Marketing promotions'},
        ),
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.AlterField(
            model_name='users',
            name='full_name',
            field=models.CharField(blank=True, max_length=200, verbose_name='Full name'),
        ),
        migrations.AlterField(
            model_name='users',
            name='id_telegram',
            field=models.IntegerField(db_index=True, verbose_name='Id Telegram'),
        ),
        migrations.AlterField(
            model_name='users',
            name='phone',
            field=models.CharField(blank=True, max_length=50, verbose_name='Phone'),
        ),
        migrations.AlterField(
            model_name='users',
            name='user_name',
            field=models.CharField(blank=True, max_length=200, verbose_name='User name'),
        ),
    ]

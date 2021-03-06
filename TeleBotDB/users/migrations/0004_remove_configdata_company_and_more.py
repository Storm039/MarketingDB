# Generated by Django 4.0.4 on 2022-04-22 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
        ('users', '0003_alter_bonuses_options_alter_company_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='configdata',
            name='company',
        ),
        migrations.RemoveField(
            model_name='marketingpromotions',
            name='company',
        ),
        migrations.AlterField(
            model_name='users',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company', verbose_name='Company'),
        ),
        migrations.DeleteModel(
            name='Bonuses',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='ConfigData',
        ),
        migrations.DeleteModel(
            name='MarketingPromotions',
        ),
    ]

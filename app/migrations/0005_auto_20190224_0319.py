# Generated by Django 2.1.7 on 2019-02-24 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20190223_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='familylist',
            name='fe',
            field=models.FloatField(default=0, verbose_name='iron'),
        ),
        migrations.AddField(
            model_name='familylist',
            name='protein',
            field=models.FloatField(default=0, verbose_name='protein'),
        ),
        migrations.AddField(
            model_name='familylist',
            name='vita',
            field=models.FloatField(default=0, verbose_name='Vit-A'),
        ),
    ]

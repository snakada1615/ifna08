# Generated by Django 2.1.3 on 2019-03-16 03:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20190316_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='familylist',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='record_date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='familylist',
            name='remark',
            field=models.CharField(default=' ', max_length=600, verbose_name='remark'),
        ),
        migrations.AlterField(
            model_name='family',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='record_date'),
        ),
    ]

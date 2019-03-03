# Generated by Django 2.1.7 on 2019-02-17 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DRI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age_id', models.IntegerField(default=1)),
                ('male_protain', models.FloatField(default=0)),
                ('male_vitA', models.FloatField(default=0)),
                ('male_fe', models.FloatField(default=0)),
                ('female_protain', models.FloatField(default=0)),
                ('female_vitA', models.FloatField(default=0)),
                ('female_fe', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='DRI_women',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=200)),
                ('female_prot2', models.FloatField(default=0)),
                ('female_vit2', models.FloatField(default=0)),
                ('female_fe2', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='FCT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FCT_id', models.IntegerField(default=1)),
                ('food_grp_id', models.IntegerField(default=1)),
                ('food_item_id', models.IntegerField(default=1)),
                ('Food_grp', models.CharField(max_length=200)),
                ('Food_name', models.CharField(max_length=200)),
                ('Crop_ref', models.CharField(max_length=200)),
                ('Edible', models.FloatField(default=0)),
                ('Energy', models.FloatField(default=0)),
                ('WATER', models.FloatField(default=0)),
                ('Protein', models.FloatField(default=0)),
                ('Fat', models.FloatField(default=0)),
                ('Carbohydrate', models.FloatField(default=0)),
                ('Fiber', models.FloatField(default=0)),
                ('ASH', models.FloatField(default=0)),
                ('CA', models.FloatField(default=0)),
                ('FE', models.FloatField(default=0)),
                ('MG', models.FloatField(default=0)),
                ('P', models.FloatField(default=0)),
                ('K', models.FloatField(default=0)),
                ('NA', models.FloatField(default=0)),
                ('ZN', models.FloatField(default=0)),
                ('CU', models.FloatField(default=0)),
                ('VITA_RAE', models.FloatField(default=0)),
                ('RETOL', models.FloatField(default=0)),
                ('B_Cart_eq', models.FloatField(default=0)),
                ('VITD', models.FloatField(default=0)),
                ('VITE', models.FloatField(default=0)),
                ('THIA', models.FloatField(default=0)),
                ('RIBF', models.FloatField(default=0)),
                ('NIA', models.FloatField(default=0)),
                ('VITB6C', models.FloatField(default=0)),
                ('FOL', models.FloatField(default=0)),
                ('VITB12', models.FloatField(default=0)),
                ('VITC', models.FloatField(default=0)),
            ],
        ),
    ]

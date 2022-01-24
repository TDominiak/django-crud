# Generated by Django 4.0.1 on 2022-01-23 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soil_sample_register', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoilSample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marking', models.IntegerField(verbose_name='Oznakowanie')),
                ('soil_category', models.CharField(max_length=30, verbose_name='Kategoria_gleby')),
                ('soil_reaction', models.FloatField(max_length=15, verbose_name='pHwKCL')),
                ('needs', models.CharField(max_length=15, verbose_name='Potrz_wapn')),
                ('chemical_element_P205', models.FloatField(max_length=100, verbose_name='P205')),
                ('chemical_element_K2O', models.FloatField(max_length=3, verbose_name='K20')),
                ('chemical_element_Mg', models.FloatField(max_length=15, verbose_name='Mg')),
                ('chemical_element_B', models.FloatField(max_length=15, verbose_name='B')),
                ('chemical_element_Mn', models.IntegerField(max_length=15, verbose_name='Mn')),
                ('chemical_element_Cu', models.FloatField(max_length=15, verbose_name='Cu')),
                ('chemical_element_Zn', models.FloatField(max_length=100, verbose_name='Zn')),
                ('chemical_element_Fe', models.IntegerField(verbose_name='Fe')),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]

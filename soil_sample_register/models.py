from django.db import models


class SoilSample(models.Model):
    sample_id = models.AutoField(primary_key=True)
    marking = models.IntegerField(verbose_name='Oznakowanie')
    soil_category = models.CharField(max_length=30, verbose_name='Kategoria_gleby')
    soil_reaction = models.FloatField(max_length=15, verbose_name='pHwKCL')
    needs = models.CharField(max_length=15, verbose_name='Potrz_wapn')

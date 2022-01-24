from django import forms

from soil_sample_register.models import SoilSample


class SoilSampleForm(forms.ModelForm):
    class Meta:
        model = SoilSample
        fields = ('marking', 'soil_category', 'soil_reaction', 'needs')
        labels = {
            'marking': 'Oznakowanie',
            'soil_category': 'Kategoria gleby',
            'soil_reaction': 'pHwKCL',
            'needs': 'Potrz_wapn',
        }

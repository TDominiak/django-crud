import django_filters

from soil_sample_register.models import SoilSample


class SoilSampleFilter(django_filters.FilterSet):
	class Meta:
		model = SoilSample
		fields = '__all__'

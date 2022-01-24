import csv
from datetime import date
from typing import List, Optional

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect

from soil_sample_register.filters import SoilSampleFilter
from soil_sample_register.forms import SoilSampleForm
from soil_sample_register.models import SoilSample


def soil_sample_exporter(request: HttpRequest):
    output: List = []
    response = HttpResponse(content_type='text/csv')
    response.write(u'\ufeff'.encode('utf8'))
    writer = csv.writer(response)
    soil_samples = SoilSample.objects.all()
    my_filter = SoilSampleFilter(request.GET, queryset=soil_samples)
    query_set = my_filter.qs
    file_name = "soil_sample_data_" + str(date.today()) + ".csv"
    response['Content-Disposition'] = 'attachment; filename = "' + file_name + '"'
    fields = ([f.name for f in SoilSample._meta.get_fields()])
    writer.writerow(fields)
    for soil_sample in query_set:
        output.append([getattr(soil_sample, str(f)) for f in fields])
    writer.writerows(output)

    return response


def soil_sample_list(request: HttpRequest):
    soil_samples = SoilSample.objects.all()
    soil_samples_with_filter = SoilSampleFilter(request.GET, queryset=soil_samples)
    soil_samples = soil_samples_with_filter.qs
    context = {'soil_sample_list': soil_samples, 'myFilter': soil_samples_with_filter}

    return render(request, 'soil_sample_register/soil_sample_list.html', context)


def soil_sample_form(request: HttpRequest, id: Optional[int] = None):
    if request.method == "GET":
        if not id:
            form = SoilSampleForm()
        else:
            soil_sample = SoilSample.objects.get(pk=id)
            form = SoilSampleForm(instance=soil_sample)
        return render(request, 'soil_sample_register/soil_sample_form.html', {'form': form})
    else:
        if not id:
            form = SoilSampleForm(request.POST)
        else:
            soil_sample = SoilSample.objects.get(pk=id)
            form = SoilSampleForm(request.POST, instance=soil_sample)
        if form.is_valid():
            form.save()

        return redirect('/list')


def soil_sample_delete(request: HttpRequest, id: int):
    employee = SoilSample.objects.get(pk=id)
    employee.delete()

    return redirect('/list')

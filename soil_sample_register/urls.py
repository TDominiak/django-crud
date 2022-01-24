from django.urls import path

from . import views

urlpatterns = [
    path('', views.soil_sample_form, name='soil_sample_insert'),
    path('<int:id>/', views.soil_sample_form, name='soil_sample_update'),
    path('delete/<int:id>/', views.soil_sample_delete, name='soil_sample_delete'),
    path('list/', views.soil_sample_list, name="soil_sample_list"),
    path('soil_sample_exporter', views.soil_sample_exporter, name="soil_sample_exporter")

]

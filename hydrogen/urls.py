from django.urls import path
from . import views

urlpatterns = [
    path('', views.hydrogen, name='hydrogen'),
    path('h2-production/', views.h2_production_view, name='h2_production'),
    path('test/', views.generic_test_view, name='generic-test'),
]

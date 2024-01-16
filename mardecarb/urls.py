from django.urls import path
from . import views

urlpatterns = [
    path('', views.mardecarb, name='mardecarb'),
]

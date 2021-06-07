from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # Data.tsv form page
    path('total', views.total, name='total'), # Total revenue page
]

from django.urls import path
from . import views


urlpatterns = [path('', views.prime_index_view, name='index')]

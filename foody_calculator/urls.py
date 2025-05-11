from django.urls import path
from . import views

app_name = 'foody_calculator'

urlpatterns = [

    path('', views.foody_calculator, name='foody_calculator'),

]

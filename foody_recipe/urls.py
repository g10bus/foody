from django.urls import path
from . import views

app_name = 'foody_recipe'

urlpatterns = [

    path('', views.foody_recipe, name='foody_recipe'),

]

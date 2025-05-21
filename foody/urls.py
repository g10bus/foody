from django.urls import path
from . import views

app_name = 'foody'

urlpatterns = [

    path('', views.foody_page, name='foody_page'),

]

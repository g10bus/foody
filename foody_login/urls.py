from django.urls import path
from . import views

app_name = 'foody_login'

urlpatterns = [

    path('', views.foody_login, name='foody_login'),

]

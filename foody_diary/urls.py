
from django.urls import path
from . import views

app_name = 'foody_diary'

urlpatterns = [

    path('', views.foody_diary, name='foody_diary'),

]

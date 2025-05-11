from django.contrib import admin
from .models import Project  #Импорт модели с текущим классом (БД) для создания проектов через amdin
# Register your models here.

admin.site.register(Project)

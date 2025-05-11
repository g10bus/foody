from django.shortcuts import render

def foody_recipe(request):
    return render(request, 'foody_recipe/foody_recipe.html')

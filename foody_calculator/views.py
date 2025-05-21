from django.shortcuts import render

def foody_calculator(request):
    return render(request, 'foody_calculator/foody_calculator.html')

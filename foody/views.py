from django.shortcuts import render

def foody_page(request):
    return render(request, 'foody/home.html')
# Create your views here.

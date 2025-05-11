from django.shortcuts import render

def foody_diary(request):
    return render(request, 'foody_diary/food_diary.html')
# Create your views here.

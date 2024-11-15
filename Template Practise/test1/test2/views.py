from django.shortcuts import render

# Create your views here.

def welcome(request):
   
    context= {'tip': 'Dei parama padidaa',}

    return render(request, 'welcome.html', context)

def favorites(request):
   
    favorite_items = ['Bhoori', 'Egg Dhosa', 'Fish', 'Rava Laddu']  # Customize this list
   
    context = {'favorites': favorite_items,}
   
    return render(request, 'favorites.html', context)
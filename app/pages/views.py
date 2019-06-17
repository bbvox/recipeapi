from django.shortcuts import render
from django.http import HttpResponse

from core.models  import Recipe

def index(request):
    recipes = Recipe.objects.order_by('-datePublished').filter(is_published=True)[:3]

    context = {
        'recipes': recipes
    }
    return render(request,'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')
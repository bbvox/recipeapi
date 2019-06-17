

from django.shortcuts import  get_object_or_404,render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse

from core.models  import Recipe 




def index(request):
   recipes = Recipe.objects.order_by('-list_date').filter(is_published=True )

   paginator = Paginator(recipes, 6)
   page = request.GET.get('page')
   paged_listings = paginator.get_page(page)
   

   context = {
      'recipes': paged_listings,
        
      
   }

   return render(request, 'listings/listings.html', context)

def listing(request, recipe_id):
   recipe = get_object_or_404(Recipe, pk=recipe_id)

   context = {
    'recipe': recipe,
   }
   
   return render(request, 'listings/listing.html',context)

def search(request):
   return render(request, 'listings/search.html')

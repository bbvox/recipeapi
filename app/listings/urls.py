from django.urls import path
from core.models import Recipe

from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:recipe_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),
    
] 
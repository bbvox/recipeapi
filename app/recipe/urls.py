from django.urls import path, include
from rest_framework.routers import DefaultRouter

from recipe import views


router = DefaultRouter()
router.register('tags', views.TagViewSet)
router.register('ingredients', views.IngredientViewSet)
router.register('recipes', views.RecipeViewSet)
router.register('aggregateRating', views.AggregateRatingViewSet)
router.register('recipeInstruction', views.RecipeInstructionViewSet)
router.register('diets', views.DietViewSet)
router.register('allergys', views.AllergyViewSet)
router.register('courses', views.CourseViewSet)
router.register('cousines', views.CousineViewSet)
router.register('holidays', views.HolidayViewSet)
router.register('nutritions', views.NutritionsViewSet)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls))
]
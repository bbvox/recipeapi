from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Tag, Ingredient, Recipe , Diet, Allergy, Course, Cousine, Holiday , Nutritions

from recipe import serializer

""""""
class DietViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Diet.objects.all()
    serializer_class = serializer.DietSerializer

    def get_queryset(self):
        assigned_only =bool(self.request.query_params.get('assigned_only'))
        queryset = self.queryset
        if assigned_only:
            queryset=queryset.filter(recipe__isnull=False)

        return queryset.filter(user=self.request.user).order_by('-name')

    def perform_create(self, serializer):
        """create Diets"""
        serializer.save(user=self.request.user)

class AllergyViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Allergy.objects.all()
    serializer_class = serializer.AllergySerializer

    def get_queryset(self):
        assigned_only =bool(self.request.query_params.get('assigned_only'))
        queryset = self.queryset
        if assigned_only:
            queryset=queryset.filter(recipe__isnull=False)

        return queryset.filter(user=self.request.user).order_by('-name')

    def perform_create(self, serializer):
        """create Allergys"""
        serializer.save(user=self.request.user)

class CourseViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Course.objects.all()
    serializer_class = serializer.CourseSerializer

    def get_queryset(self):
        assigned_only =bool(self.request.query_params.get('assigned_only'))
        queryset = self.queryset
        if assigned_only:
            queryset=queryset.filter(recipe__isnull=False)

        return queryset.filter(user=self.request.user).order_by('-name')

    def perform_create(self, serializer):
        """create Courses"""
        serializer.save(user=self.request.user)

class CousineViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Cousine.objects.all()
    serializer_class = serializer.CousineSerializer

    def get_queryset(self):
        assigned_only =bool(self.request.query_params.get('assigned_only'))
        queryset = self.queryset
        if assigned_only:
            queryset=queryset.filter(recipe__isnull=False)

        return queryset.filter(user=self.request.user).order_by('-name')

    def perform_create(self, serializer):
        """create Cousines"""
        serializer.save(user=self.request.user)

class HolidayViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Holiday.objects.all()
    serializer_class = serializer.HolidaySerializer

    def get_queryset(self):
        assigned_only =bool(self.request.query_params.get('assigned_only'))
        queryset = self.queryset
        if assigned_only:
            queryset=queryset.filter(recipe__isnull=False)

        return queryset.filter(user=self.request.user).order_by('-name')

    def perform_create(self, serializer):
        """create Holidays"""
        serializer.save(user=self.request.user)

class NutritionsViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Nutritions.objects.all()
    serializer_class = serializer.NutritionsSerializer

    def get_queryset(self):
        assigned_only =bool(self.request.query_params.get('assigned_only'))
        queryset = self.queryset
        if assigned_only:
            queryset=queryset.filter(recipe__isnull=False)

        return queryset.filter(user=self.request.user).order_by('-name')

    def perform_create(self, serializer):
        """create Nutritions"""
        serializer.save(user=self.request.user)


""""""


class TagViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Tag.objects.all()
    serializer_class = serializer.TagSerializer

    def get_queryset(self):
        assigned_only =bool(self.request.query_params.get('assigned_only'))
        queryset = self.queryset
        if assigned_only:
            queryset=queryset.filter(recipe__isnull=False)

        return queryset.filter(user=self.request.user).order_by('-name')

    def perform_create(self, serializer):
        """create tags"""
        serializer.save(user=self.request.user)


class IngredientViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Ingredient.objects.all()
    serializer_class = serializer.IngredientSerializer

    def get_queryset(self):
        assigned_only =bool(self.request.query_params.get('assigned_only'))
        queryset = self.queryset
        if assigned_only:
            queryset=queryset.filter(recipe__isnull=False)

        return queryset.filter(user=self.request.user).order_by('-name')

    def perform_create(self, serializer):
        """create new ingred"""
        serializer.save(user=self.request.user)    


class RecipeViewSet(viewsets.ModelViewSet):
    """manage recipe in db"""
    serializer_class = serializer.RecipeSerializer
    queryset = Recipe.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def _params_to_ints(self,qs):
        return [int(str_id) for str_id in qs.split(',')]


    def get_queryset(self):
        """retrive the recipe for the authenticated user"""
        tags = self.request.query_params.get('tags')
        ingredients = self.request.query_params.get('ingredients')
        """"""
        diets = self.request.query_params.get('diets')
        allergys = self.request.query_params.get('Allergys')
        courses = self.request.query_params.get('courses')
        cousines = self.request.query_params.get('cousines')
        holidays = self.request.query_params.get('holidays')
        nutritions = self.request.query_params.get('nutritions')
        """"""
        
        queryset = self.queryset
        if tags:
            tag_ids=self._params_to_ints(tags)
            queryset =queryset.filter(tags__id__in=tag_ids)
        if ingredients:
            ingredient_ids = self._params_to_ints(ingredients)
            queryset = queryset.filter(ingredients__id__in=ingredient_ids)
        """"""
        if diets:
            diet_ids=self._params_to_ints(diets)
            queryset =queryset.filter(diets__id__in=diet_ids)

        if allergys:
            allergy_ids=self._params_to_ints(allergys)
            queryset =queryset.filter(allergys__id__in=allergy_ids)

        if courses:
            course_ids=self._params_to_ints(courses)
            queryset =queryset.filter(courses__id__in=course_ids)

        if cousines:
            cousine_ids=self._params_to_ints(cousines)
            queryset =queryset.filter(cousines__id__in=cousine_ids)
            
        if holidays:
            holiday_ids=self._params_to_ints(holidays)
            queryset =queryset.filter(holidays__id__in=holiday_ids)

        if nutritions:
            nutritions_ids=self._params_to_ints(nutritions)
            queryset =queryset.filter(nutritions__id__in=nutritions_ids)
        """"""    

        return queryset.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'retrive':
            return serializer.RecipeDetailSerializer
        elif self.action == 'upload_image':
            return serializer.RecipeImageSerializer
        
        return self.serializer_class 


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(methods=['POST'], detail=True, url_path='upload-image')
    def upload_image(self, request, pk=None):
        recipe = self.get_object()
        serializer = self.get_serializer(
            recipe,
            data = request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status= status.HTTP_400_BAD_REQUEST
    
        )    

          




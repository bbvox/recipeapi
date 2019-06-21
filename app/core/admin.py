from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from core import models


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )

class RecipeAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'is_published', 'estimatedCost', 'datePublished','description','keywords')
  list_display_links = ('id', 'name')
  list_filter = ('user',)
  list_editable = ('is_published',)
  search_fields = ('name', 'description','estimatedCost')
  list_per_page = 25



admin.site.register(models.User, UserAdmin)

admin.site.register(models.RecipeInstruction)
admin.site.register(models.AggregateRating)
admin.site.register(models.Tag)
admin.site.register(models.Ingredient)
admin.site.register(models.Recipe, RecipeAdmin)
admin.site.register(models.Diet)
admin.site.register(models.Allergy)
admin.site.register(models.Course)
admin.site.register(models.Cousine)
admin.site.register(models.Holiday)
admin.site.register(models.Nutritions)
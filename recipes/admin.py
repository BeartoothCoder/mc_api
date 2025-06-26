from django.contrib import admin
from .models import Recipe

# Register your models here.
@admin.register(Recipe)
class RecipeModel(admin.ModelAdmin):
    fields = ['data', 'img_link']
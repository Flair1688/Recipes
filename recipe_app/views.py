from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Recipe


class RecipeList(ListView):
    model = Recipe
    template_name = 'recipe_list.html'
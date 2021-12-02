from django.views.generic import ListView, DetailView
from .models import Recipe
from django.shortcuts import render, get_object_or_404


class RecipeList(ListView):
    model = Recipe
    template_name = 'recipe_list.html'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe_app/recipe_detail.html'

    #def recipe_detail(request, pk):
     #   recipe = get_object_or_404(Recipe, pk=pk)
      #  return render(request, 'recipe_app/recipe_detail.html', {'recipe': recipe})
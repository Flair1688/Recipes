from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import RecipeList, RecipeDetailView

urlpatterns = [
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('', RecipeList.as_view(), name='recipe_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import RecipeList

urlpatterns = [
    path('', RecipeList.as_view(), name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
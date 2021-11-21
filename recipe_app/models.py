from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='название')


class Ingredient(models.Model):
    name = models.CharField(max_length=50, verbose_name='название')


class Recipe(models.Model):
    user = models.ForeignKey(User,  on_delete=models.CASCADE, null=True, blank=True)
    create = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    number = models.IntegerField() # Количество порций
    video = models.FileField(upload_to='recipe_app/videos/', blank=True, null=True, verbose_name="")
    #category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    img = models.ImageField(upload_to='recipe_app/images', blank=True)

    def __str__(self):
        return self.title


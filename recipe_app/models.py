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
    description = models.TextField(null=True, blank=False)
    #number = models.IntegerField()
    video = models.FileField(upload_to='videos/%Y/%m/%d', blank=True, null=True, verbose_name="")
    #category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    image = models.ImageField(blank=True, upload_to='images/%Y/%m/%d', verbose_name='Ссылка картинки')

    def __str__(self):
        return self.title






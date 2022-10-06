from turtle import update
from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_lenght=65)
    description = models.CharField(max_lenght=165)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_lenght=65)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_lenght=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(defalt=False)
    creatd_at = models.DateTimeField(auto_now_add=True)
    update_at = models.models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(defalt=False)
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/')
    
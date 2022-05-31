from operator import mod
from versatileimagefield.fields import VersatileImageField

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField()

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    categories = models.ManyToManyField(Category, related_name="courses")
    name = models.CharField(max_length=20)
    slug = models.SlugField()
    article = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = VersatileImageField(upload_to="product", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["article"]

    def __str__(self):
        return self.name
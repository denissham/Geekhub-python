from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    category_fk = models.ForeignKey('Category', on_delete=models.CASCADE, default=None, null=True)
    name = models.CharField(max_length=200, default='')
    description = models.TextField(default='', blank=True)
    sku = models.CharField(max_length=100, default='')
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(decimal_places=2, max_digits=9, default=0)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name + ('' if self.is_active else ' (disabled)')

    def get_absolute_url(self):
        return reverse('products:product_detail', args=[self.id])

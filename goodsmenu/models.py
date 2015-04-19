# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Category(models.Model):
    class Meta:
        db_table = "category"
        verbose_name = "Категория"
        verbose_name_plural = "категории"

    Title = models.CharField(max_length=50, verbose_name="Название")
    Description = models.TextField(verbose_name="Описание", null=True)

    def __unicode__(self):
        return self.title


class Product(models.Model):
    class Meta:
        db_table = "product"
        verbose_name = "Товар"
        verbose_name_plural = "товары"

    Title = models.CharField(max_length=200, verbose_name="Название")
    Title_English = models.CharField(max_length=200, verbose_name="НазваниеПоАнглийски")
    Price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Цена")
    Description = models.TextField(verbose_name="Описание")
    ProductCategory = models.ForeignKey(Category, verbose_name="Категория")
    Discount = models.FloatField(verbose_name="Скидка")
    Status = models.BooleanField(default=False, verbose_name="Статус")
    Photo = models.ImageField(upload_to='uploads/productimages', verbose_name="Фото")
    Weight = models.FloatField(verbose_name="Вес")
    Diameter = models.FloatField(verbose_name="Диаметр")
    Ingredients = models.TextField(verbose_name="Ингридиенты")

    def __unicode__(self):
        return self.title



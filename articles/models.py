# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Articles(models.Model):
    class Meta:
        db_table = "articles"
        verbose_name = "Статья"
        verbose_name_plural = "статьи"

    Title = models.CharField(max_length=250, verbose_name="Название")
    Description = models.TextField(verbose_name="Текст", null=True)
    Author = models.CharField(max_length=50, verbose_name="Автор")
    Date = models.DateTimeField(verbose_name="ДатаРазмещения")
    Photo = models.ImageField(upload_to='uploads/articleimages', blank=True, verbose_name="Фото")

    def __unicode__(self):
        return self.title

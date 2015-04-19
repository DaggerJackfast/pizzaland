# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

"""class Order_Good(models.Model):
    class Meta:
        db_table = "order"
        verbose_name = "Заказ"
        verbose_name_plural = "заказы"
    ID_Order = models.ForeignKey(Order)
    ID_Product = models.ForeignKey(models.Product)
    CountProducts = models.IntField(default=0)

    def __unicode__(self):
        return self.title

class Order(models.Model):
    class Meta:
        db_table = "order"
        verbose_name = "Заказ"
        verbose_name_plural = "заказы"
    Client = models.ForeignKey()
    Title = models.CharField(max_length=50, verbose_name="Название")
    Description = models.TextField(verbose_name="Описание", null=True)

    def __unicode__(self):
        return self.title
        """



django-admin startproject ecommerce 
django-admin startapp products 
django-admin register app products 
product model prepration 
from django.db import models 
class product(models.Model):
name = models.CharField(max_length = 100)
price = models.IntegerField()
stock = models.Integerfiels()

def__str__(self):
return self.name

from django.db import models 
class books(models.Model):
title = models.CharFiels(max_length = 100)
author = models.CharField(max_length = 100)
pages = models.interfields()

def__str__(self):
return books.title:
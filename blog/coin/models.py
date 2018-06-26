from django.db import models
from ckeditor.fields import RichTextField
from django.contrib import admin

# Create your models here.

class Coin(models.Model):
    author = models.CharField(max_length = 20, verbose_name = "Coin Sahibi")
    content = models.TextField(verbose_name = "Neden")
    quantity = models.CharField(max_length = 10, verbose_name = "Miktar")

    def __str__(self):
        return self.author

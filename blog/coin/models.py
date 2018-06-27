from django.db import models
from ckeditor.fields import RichTextField
from django.contrib import admin

# Create your models here.

class Coin(models.Model):
    author = models.ForeignKey("auth.User", on_delete = models.CASCADE, verbose_name = "Yazar")
    content = models.TextField(verbose_name = "Neden")
    quantity = models.CharField(max_length = 10, verbose_name = "Miktar")
    created_date = models.DateTimeField(auto_now_add = True, verbose_name = "Oluşturulma Tarihi")
    
    def __str__(self):
        return self.author

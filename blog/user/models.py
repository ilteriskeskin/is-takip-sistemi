from django.db import models

# Create your models here.

class Users(models.Model):
        created_date = models.DateTimeField(auto_now_add = True, verbose_name = "Oluşturulma Tarihi")
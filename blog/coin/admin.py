from django.contrib import admin
from .models import Coin

# Register your models here.

@admin.register(Coin)
class CoinAdmin(admin.ModelAdmin):
    list_display = ('author', 'content','quantity')
    list_link = ('author')

    class Meta:
        model = Coin
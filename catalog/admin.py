from django.contrib import admin
from .models import Client,Order,Pizza,Category


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ['id','tittle','city']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id','phone','firstName','city']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','client','status']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','category']
from django.contrib import admin
from .models import Product, Transaction, Category


class TransactionAdmin(admin.ModelAdmin):
    list_display = ['status', 'from_where', 'to_where']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'available', 'on_stock')
    search_fields = ('title', 'available', 'on_stock')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Transaction, TransactionAdmin)
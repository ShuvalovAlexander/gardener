from django.contrib import admin
from .models import Product, Feedback
from .models import Order
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'old_price')
    fields = ('title', 'description', 'price', 'old_price', 'image', 'additional_image', 'characteristics')

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'agree') 

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'email', 'price', 'created_at')
    search_fields = ('product', 'email', 'phone')
    readonly_fields = ('created_at',)
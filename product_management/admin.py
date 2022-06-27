from django.contrib import admin
from product_management.models import Product, History
# Register your models here.


class HistoryInline(admin.TabularInline):
    model = History
    extra = 0
    readonly_fields = ['created_at', 'price']
    fields = ['price', 'action', 'quantity', 'created_at']
    ordering = ['-created_at']


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ['quantity']
    search_fields = ['name']
    list_filter = ['price']
    fieldsets = [
        ('Information', {
            'fields': ['name', 'price', 'quantity']
        }),
    ]

    list_display = ['id', 'name', 'price', 'quantity']
    list_display_links = ['id', 'name']
    inlines = [HistoryInline]


class HistoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Product', {
            'fields': ['product', 'price']
        }),
        ('Quantity', {
            'fields': ['action', 'quantity']
        }),
    ]

    list_display = ['id', 'created_at', 'product', 'price', 'action', 'quantity']
    list_display_links = ['id', 'product']


admin.site.register(Product, ProductAdmin)
admin.site.register(History, HistoryAdmin)

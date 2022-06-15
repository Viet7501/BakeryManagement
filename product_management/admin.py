from django.contrib import admin
from product_management.models import Product, History

# Register your models here.


class HistoryInline(admin.TabularInline):
    model = History
    extra = 0
    readonly_fields = ['created_at']
    fields = ['price', 'add_quantity', 'expired_quantity', 'inventory_quantity', 'created_at']


class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Information', {
            'fields': ['name', 'price', 'quantity']
        }),
    ]

    list_display = ['name', 'price', 'quantity']
    list_display_links = ['name']
    inlines = [HistoryInline]


class HistoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Product', {
            'fields': ['product', 'price']
        }),
        ('Quantity', {
            'fields': ['add_quantity', 'expired_quantity', 'inventory_quantity']
        }),
    ]

    list_display = ['created_at', 'product', 'price', 'inventory_quantity', 'add_quantity', 'expired_quantity',
                    'subtotal']
    list_display_links = ['product']


admin.site.register(Product, ProductAdmin)
admin.site.register(History, HistoryAdmin)

from django.contrib import admin
from money_management.models import Category, Transaction


# Register your models here.


class TransactionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Information', {
            'fields': ['category', 'name', 'amount', 'note']
        }),
    ]

    list_display = ['category', 'name', 'amount', 'note']
    list_display_links = ['name']


class TransactionInline(admin.TabularInline):
    model = Transaction
    extra = 0
    fields = ['name', 'amount', 'note']


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Information', {
            'fields': ['name']
        }),
    ]
    list_display = ['name']
    list_display_links = ['name']
    inlines = [TransactionInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Transaction, TransactionAdmin)

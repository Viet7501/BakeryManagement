from django.contrib import admin
from money_management.models import Category, Transaction


# Register your models here.


class TransactionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Information', {
            'classes': ('grp-collapse grp-open',),
            'fields': ['category', 'name', 'amount', 'note']
        }),
    ]
    list_display = ['id', 'category', 'name', 'amount', 'note']
    list_display_links = ['id', 'name']


class TransactionInline(admin.TabularInline):
    model = Transaction
    extra = 0
    readonly_fields = ['created_at']
    fields = ['name', 'amount', 'note', 'created_at']


class CategoryAdmin(admin.ModelAdmin):
    list_filter = ['name']
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

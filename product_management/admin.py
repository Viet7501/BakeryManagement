from django.contrib import admin
from product_management.models import Product, History
from django.utils.translation import gettext_lazy as _


# Register your models here.


class HistoryInline(admin.TabularInline):
    model = History
    extra = 0
    readonly_fields = ['created_at', 'price']
    fields = ['price', 'action', 'quantity', 'created_at']
    ordering = ['-created_at']


class PriceFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('filter by price')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'decade'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('0-5', _('0-5')),
            ('5-10', _('5-10')),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value() == '0-5':
            return queryset.filter(
                price__gte=0,
                price__lte=5,
            )
        if self.value() == '5-10':
            return queryset.filter(
                price__gte=5,
                price__lte=10,
            )


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ['quantity']
    search_fields = ['name']
    list_filter = [PriceFilter, ]
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

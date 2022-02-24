from django.contrib import admin
from .models import Stock
from .forms import StockCreateForm


class StockCreateAdmin(admin.ModelAdmin):
    list_display = ['category', 'item_name', 'quantity']
    form = StockCreateForm
    # allow us to filter by category to the admin site
    list_filter = ['category']
    # allow us to make search field on admin site
    search_fields = ['category', 'item_name']


admin.site.register(Stock,  StockCreateAdmin)

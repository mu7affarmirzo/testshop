from django.contrib import admin
from .models import OrderItemModel, OrderModel

class OrderItemInline(admin.TabularInline):
    model = OrderItemModel
    raw_id_fields = ['product']

@admin.register(OrderModel)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'paid',
                    'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]
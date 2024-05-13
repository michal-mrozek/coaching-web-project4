
from django.contrib import admin
from .models import Order, OrderItem


class OrderItemAdminInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('membership_length', 'membership_price',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemAdminInline,)
    readonly_fields = ('order_number', 'date', 'order_total',
                       'stripe_pid')

    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address',
              'order_total', 'stripe_pid')

    list_display = ('order_number', 'date', 'full_name',
                    'order_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)


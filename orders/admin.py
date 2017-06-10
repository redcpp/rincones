from django.contrib import admin

from .models import Order

class OrderAdmin(admin.ModelAdmin):
    date_hierarchy = 'timestamp'
    list_display = ('order_id', 'user', 'state', 'finished', 'updated')
    list_filter = ('finished', 'state')
    readonly_fields = ('updated', 'timestamp')
    search_fields = ('order_id',)

admin.site.register(Order, OrderAdmin)

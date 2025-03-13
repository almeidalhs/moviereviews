from django.contrib import admin
from .models import Cart

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'item_count')
    search_fields = ('user__username',)

    def item_count(self, obj):
        return obj.items.count()
    item_count.short_description = 'Items'

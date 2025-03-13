from django.contrib import admin
from .models import Order, OrderItem
from django.utils.html import format_html
from django.urls import reverse
from django.utils.safestring import mark_safe

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'order_id',
        'user_info',
        'status_badge',
        'order_items_link',
        'total_amount',
        'created_at',

    )
    list_filter = ('status', 'created_at')

    def order_id(self, obj):
        return f"ORDER-{obj.id:08d}"

    order_id.short_description = 'Order ID'

    def user_info(self, obj):
        return format_html(
            '{}<br><small>{}</small>',
            obj.user.username,
            obj.user.email
        )

    user_info.short_description = 'Customer'

    def status_badge(self, obj):
        color_map = {
            'pending': 'orange',
            'completed': 'green',
            'canceled': 'red'
        }
        return format_html(
            '<span style="color: white; background-color: {};'
            'padding: 5px; border-radius: 5px;">{}</span>',
            color_map.get(obj.status, 'gray'),
            obj.get_status_display().upper()
        )

    status_badge.short_description = 'Status'

    def order_items_link(self, obj):
        url = (
                reverse('admin:orders_orderitem_changelist')
                + f'?order__id__exact={obj.id}'
        )
        count = obj.items.count()
        return format_html(
            '<a href="{}" class="order-items-link">View Items ({})</a>',
            url,
            count
        )

    order_items_link.short_description = 'Items'
    order_items_link.allow_tags = True

    # 优化查询
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('items')

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        'movie_title',
        'order_link',
        'quantity',
        'price',
        'item_total'
    )
    list_select_related = ('movie', 'order')

    def movie_title(self, obj):
        return obj.movie.title
    movie_title.short_description = 'Movie'

    def order_link(self, obj):
        url = reverse('admin:orders_order_change', args=[obj.order.id])
        return format_html('<a href="{}">{}</a>', url, obj.order)
    order_link.short_description = 'Order'

    def item_total(self, obj):
        return obj.quantity * obj.price
    item_total.short_description = 'Total'

    def get_queryset(self, request):
        return super().get_queryset(request).select_related(
            'movie', 'order__user'
        )
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order

@receiver(post_save, sender=Order)
def update_order_status(sender, instance, created, **kwargs):
    if created and instance.status == 'pending':
        # 此处可添加支付接口调用
        pass
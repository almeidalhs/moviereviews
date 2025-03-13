from django.shortcuts import redirect
from django.views.generic import View, ListView, DetailView, TemplateView,CreateView
from .models import Order, OrderItem
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect

class CreateOrderView(CreateView):
    model = Order
    template_name = 'orders/order_form.html'
    fields = []

    def get_context_data(self, **kwargs):
        """add cart context to the template"""
        context = super().get_context_data(**kwargs)
        context['cart'] = self.request.user.cart
        return context

    def form_valid(self, form):
        cart = self.request.user.cart

        if not cart.items.exists():
            form.add_error(None, "Cannot place empty order")
            return self.form_invalid(form)

        order = form.save(commit=False)
        order.user = self.request.user
        order.total_amount = sum(item.total_price for item in cart.items.all())
        order.save()

        for cart_item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                movie=cart_item.movie,
                quantity=cart_item.quantity,
                price=cart_item.movie.price
            )

        cart.items.all().delete()
        return redirect('orders:order_detail', pk=order.pk)

class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'order_detail.html'
    context_object_name = 'order'

    def get_queryset(self):
        """确保用户只能查看自己的订单"""
        return super().get_queryset().filter(user=self.request.user)


class CancelOrderView(LoginRequiredMixin, View):
    def post(self, request, pk):
        order = get_object_or_404(Order, pk=pk, user=request.user)
        if order.status == 'pending':
            order.status = 'canceled'
            order.save()
        return redirect('orders:order_detail', pk=pk)


class PayOrderView(LoginRequiredMixin, View):
    def post(self, request, pk):
        order = get_object_or_404(
            request.user.orders.all(),
            pk=pk,
            status='pending'
        )

        # 模拟支付成功
        order.status = 'completed'
        order.save()

        messages.success(request, "Payment completed successfully!")
        return redirect('orders:order_detail', pk=pk)


class PaymentSuccessView(TemplateView):
    template_name = 'orders/payment_success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order'] = get_object_or_404(
            self.request.user.orders,
            pk=self.kwargs['pk']
        )
        return context



class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'orders/order_list.html'
    context_object_name = 'orders'
    paginate_by = 10

    def get_queryset(self):
        return self.request.user.orders.all() \
            .prefetch_related('items') \
            .order_by('-created_at')
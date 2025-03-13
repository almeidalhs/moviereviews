from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView
from .models import Cart, CartItem
from movie.models import Movie
from django.core.exceptions import PermissionDenied

class CartDetailView(DetailView):
    model = Cart
    template_name = 'cart_detail.html'

    def get_object(self):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return cart

    def dispatch(self, request, *args, **kwargs):
        try:
            return super().dispatch(request, *args, **kwargs)
        except Cart.DoesNotExist:
            if request.user.is_authenticated:
                # 如果信号系统失效时的备用方案
                Cart.objects.create(user=request.user)
                return redirect(self.request.path)
            raise PermissionDenied


def add_to_cart(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        movie=movie,
        defaults={'quantity': 1}
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart:cart_detail')


def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, pk=item_id, cart=request.user.cart)
    cart_item.delete()
    return redirect('cart:cart_detail')

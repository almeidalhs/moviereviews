from django.conf import settings
from django.db import models
from movie.models import Movie
from django.db.models import Sum, F

class Cart(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='cart'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_amount(self):
        """Real-time calculation using database aggregation"""
        return self.items.aggregate(
            total=Sum(F('quantity') * F('movie__price'))
        )['total'] or 0


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_price(self):
        return self.movie.price * self.quantity

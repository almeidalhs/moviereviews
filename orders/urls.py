from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('create/', views.CreateOrderView.as_view(), name='create_order'),
    path('<int:pk>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('<int:pk>/cancel/', views.CancelOrderView.as_view(), name='cancel_order'),
    path('<int:pk>/pay/', views.PayOrderView.as_view(), name='pay_order'),
    path('my-orders/', views.OrderListView.as_view(), name='order_list'),


]
from django.db import models

from accounts.models import CartItem


def common_context(request):
    cart_items = []
    total_amount = 0
    cart_items_count = 0

    if request.user.is_authenticated:
        try:
            cart_items = CartItem.objects.filter(cart=request.user.cart).annotate(
                total_amount=models.F('quantity') * models.F('product__price')
            )
            total_amount = sum(item.total_amount for item in cart_items)
            cart_items_count = request.user.cart.cart_items.count()
        except Exception:
            pass

    return {
        'site_name': 'VooCommerce',
        'is_user_authenticated': request.user.is_authenticated,
        'user_cart_items_count': cart_items_count,
        'cart_total_amount': total_amount / 100
    }
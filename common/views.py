from django.views.generic import TemplateView
from django.db import models
from products.models import Category
from accounts.models import CartItem


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        categories = Category.objects.all()
        context['title'] = 'eCommerce | Home'
        context['categories'] = categories
        return context
    

class ContactView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'eCommerce | Contact us'
        return context
    
class BlogView(TemplateView):
    template_name = 'blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'eCommerce | Blog'
        return context
    

class BlogDetailsView(TemplateView):
    template_name = 'blog-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'eCommerce | Blog Details'
        return context
    
class CheckoutView(TemplateView):
    template_name = 'checkout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'eCommerce | Checkout'
        return context
    

class ShopDetailsView(TemplateView):
    template_name = 'shop-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'eCommerce | Shop Details'
        return context


class ShopGridView(TemplateView):
    template_name = 'shop-grid.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'eCommerce | Shop Grid'
        return context


class ShopingCartView(TemplateView):
    template_name = 'shopping-cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'eCommerce | Shopping Cart'

        try:
            cart = self.request.user.cart
            cart_items = CartItem.objects.filter(cart=cart).annotate(
                total_amount=models.F('quantity') * models.F('product__price')
            )
            total_amount = sum(item.total_amount for item in cart_items)

            context['cart_items'] = cart_items
            context['total_amount'] = total_amount
        except AttributeError:
            # Cart does not exist
            context['cart_items'] = []
            context['total_amount'] = 0

        return context



from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nexkart | Home'
        return context
    

class ContactView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nexkart | Contact Us'
        return context
    

class ShopView(TemplateView):
    template_name = 'shop-grid.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nexkart | Shop'
        return context
    

class ShopDetailView(TemplateView):
    template_name = 'shop-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nexkart | Shop Detail'
        return context
    

class ShopingCartView(TemplateView):
    template_name = 'shoping-cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nexkart | Shopping Cart'
        return context


class PagesView(TemplateView):
    template_name = 'pages.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nexkart | Pages'
        return context
    

class BlogView(TemplateView):
    template_name = 'blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nexkart | Blog'
        return context
        

class CheckOutView(TemplateView):
    template_name = 'checkout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nexkart | Checkout'
        return context
    

class BlogDetailView(TemplateView):
    template_name = 'blog-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nexkart | Blog Detail'
        return context

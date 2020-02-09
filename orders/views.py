from django.shortcuts import render
from django.views.generic.list import ListView
from orders.models import Product
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(login_required, name='dispatch')
class ProductView(ListView):
    model = Product
    template_name = 'orders/orders_list.html'
    paginate_by = 24

    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        return context


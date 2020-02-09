from django.conf.urls import url,include
from django.contrib import admin
from orders.views import ProductView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/',include('accounts.urls')),
    url(r'^$', ProductView.as_view(), name="home"),
    #url(r'^orders/',include('orders.urls')),
]

from django.conf.urls import url,include
from django.contrib import admin
from orders.views import ProductView
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/',include('accounts.urls')),
    url(r'^$', ProductView.as_view(), name="home"),
    #url(r'^orders/',include('orders.urls')),
    url(r'^password_reset/$', auth_views.password_reset,{'template_name': 'layout/password_reset_form.html'}, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done,{'template_name': 'layout/password_reset_done.html'}, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm,{'template_name':'layout/password_reset_confirm.html'}, name='password_reset_confirm'),
    url(r'^reset/done/$',auth_views.password_reset_complete,{'template_name':'layout/password_reset_complete.html'}, name='password_reset_complete'),
]

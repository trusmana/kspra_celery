from django.conf.urls import url
from .views import ProductView
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^product/$', ProductView.as_view(), name="product"),
]

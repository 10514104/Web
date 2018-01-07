from django.conf.urls import url
from shop import views


urlpatterns = [
    url(r'^$', views.shop, name='shop'),
    url(r'^checkout/$', views.checkout, name='checkout'),
    url(r'^order/$', views.order, name='order'),
    url(r'^shopDelete/(?P<shopId>[0-9]+)/$', views.shopDelete, name='shopDelete'),
]


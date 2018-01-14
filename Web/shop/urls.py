from django.conf.urls import url
from shop import views


urlpatterns = [
    url(r'^$', views.shop, name='shop'),
    url(r'^checkout/$', views.checkout, name='checkout'),
    url(r'^order/$', views.order, name='order'),
    url(r'^shopDelete/(?P<shopId>[0-9]+)/$', views.shopDelete, name='shopDelete'),
    url(r'^fin/$', views.fin, name='fin'),
    url(r'^fin2/$', views.fin2, name='fin2'),
]


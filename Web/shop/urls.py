from django.conf.urls import url
from shop import views


urlpatterns = [
    url(r'^$', views.shop, name='shop'),
    url(r'^checkout/$', views.checkout, name='checkout'),
]
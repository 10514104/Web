from django.conf.urls import url
from main import views


urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^mainProduct/(?P<productId>[0-9]+)/$', views.mainProduct, name='mainProduct'),
]
from django.conf.urls import url
from . import views

urlpatterns = [
    url('^carts/$', views.CartView.as_view(),name='info'),
    url('^carts/selection/$', views.CartSelectionView.as_view()),
    url('^carts/simple/$', views.CartSimpleView.as_view()),
]

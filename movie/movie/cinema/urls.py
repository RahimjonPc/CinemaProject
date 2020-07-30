from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('info', views.info, name='information'),
    path('order', views.order, name='order'),
    path('thanks', views.thanks, name='thanks'),
]
from django.conf.urls import url
from . import views

app_name = 'promo'

urlpatterns = [
    url('promo/create/', views.PromoCreateAPI.as_view(), name='create'),
    url('promo/check/', views.PromoCheckAPI.as_view(), name='check'),
]

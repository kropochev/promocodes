from .models import PromoCreate, PromoCheck
from rest_framework import serializers


class PromoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromoCreate
        fields = ('amount', 'group',)


class PromoCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromoCheck
        fields = ('promo_code',)

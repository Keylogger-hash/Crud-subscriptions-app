from rest_framework import serializers
from subscriptions_api.models import Subscriptions


class SubscriptionsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriptions
        fields = "__all__"
        # fields = ('name','currency','price','description','created_at','updated_at')

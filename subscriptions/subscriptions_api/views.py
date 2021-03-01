from django.shortcuts import render
from subscriptions_api.models import Subscriptions
from rest_framework import generics
from subscriptions_api.serializers import SubscriptionsListSerializer
# Create your views here
class ListSubscriptions(generics.ListCreateAPIView):
    queryset = Subscriptions.objects.all()
    serializer_class = SubscriptionsListSerializer


class SubscriptionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subscriptions.objects.all()
    serializer_class = SubscriptionsListSerializer

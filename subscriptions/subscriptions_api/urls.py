from django.urls import path, include
from subscriptions_api import views


urlpatterns = [
    path("subscriptions/",views.ListSubscriptions.as_view()),
    path("subscriptions/<int:pk>/",views.SubscriptionDetail.as_view())
]

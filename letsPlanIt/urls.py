from django.urls import include, path

from rest_framework import routers

from letsPlanIt.views import PersonViewSet, EventViewSet, SubscriptionViewSet, PaymentHistoryViewSet

router = routers.DefaultRouter()
router.register(r'person', PersonViewSet)
router.register(r'events', EventViewSet)
router.register(r'subscriptions', SubscriptionViewSet)
router.register(r'payment_history', PaymentHistoryViewSet)

urlpatterns = [
   path('', include(router.urls)),
]
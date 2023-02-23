from django.urls import include, path

from rest_framework import routers

from church.views import PersonViewSet, EventViewSet

router = routers.DefaultRouter()
router.register(r'person', PersonViewSet)
router.register(r'events', EventViewSet)

urlpatterns = [
   path('', include(router.urls)),
]
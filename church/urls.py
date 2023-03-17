from django.urls import include, path

from rest_framework import routers

from church.views import PersonViewSet, EventViewSet, CellViewSet

router = routers.DefaultRouter()
router.register(r'person', PersonViewSet)
router.register(r'events', EventViewSet)
router.register(r'cells', CellViewSet)

urlpatterns = [
   path('', include(router.urls)),
]
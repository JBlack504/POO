from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmpleadorViewSet, OfertaViewSet, HabilidadViewSet, ResenaViewSet

router = DefaultRouter()

router.register(r'empleadores',EmpleadorViewSet)
router.register(r'ofertas',OfertaViewSet)
router.register(r'habilidades', HabilidadViewSet)
router.register(r'resenas', ResenaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

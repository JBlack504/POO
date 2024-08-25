from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmpresaViewSet, OfertaViewSet, HabilidadViewSet, ResenaViewSet

router = DefaultRouter()

router.register(r'empleadores',EmpresaViewSet)
router.register(r'ofertas',OfertaViewSet)
router.register(r'habilidades', HabilidadViewSet)
router.register(r'resenas', ResenaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

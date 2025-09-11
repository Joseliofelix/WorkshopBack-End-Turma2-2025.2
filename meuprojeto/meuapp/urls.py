from django.urls import path, include
from rest_framework import routers
from .viewsets import CepViewSet

router = routers.DefaultRouter()
router.register(r'ceps', CepViewSet, basename='cep')

urlpatterns = [
    path('api/', include(router.urls)),
]

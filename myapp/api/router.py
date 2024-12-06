from rest_framework.routers import DefaultRouter
from myapp.api.views import ModelosNexuViewSet

router_ModelosNexu = DefaultRouter()
router_ModelosNexu.register(prefix='Modelos', basename='post', viewset= ModelosNexuViewSet)
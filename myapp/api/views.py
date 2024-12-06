from rest_framework.viewsets import ModelViewSet
from myapp.models import Modelos_nexu
from myapp.api.serializers import ModelosNexuSerializer

class ModelosNexuViewSet(ModelViewSet):
    serializer_class = ModelosNexuSerializer
    queryset = Modelos_nexu.objects.all()
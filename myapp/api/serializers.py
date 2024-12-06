from rest_framework.serializers import ModelSerializer
from myapp.models import Modelos_nexu

class ModelosNexuSerializer(ModelSerializer):
    class Meta:
        model = Modelos_nexu
        fields = ['id','name','average_price','brand_name']
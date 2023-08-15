from rest_framework.serializers import ModelSerializer
from .models import Urls

class urlShortenerSerializer(ModelSerializer):
    class Meta:
        model = Urls
        fields = ['longurl', 'shorturl']
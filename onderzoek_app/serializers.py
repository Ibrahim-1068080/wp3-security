from rest_framework import serializers
from .models import Onderzoek

class OnderzoekSerializer(serializers.ModelSerializer):
    class Meta:
        model = Onderzoek
        fields = '__all__'

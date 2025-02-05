from rest_framework import serializers

from .models import City


class CitySerializer(serializers.Serializer):
    name = serializers.CharField(help_text="Название города",
                                 max_length=255)
    latitude = serializers.FloatField(help_text="Широта города")
    longitude = serializers.FloatField(help_text="Долгота города")

    class Meta:
        model = City
        fields = '__all__'

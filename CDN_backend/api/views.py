from django.db.models import ExpressionWrapper, F, FloatField
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import City
from .serializers import CitySerializer
from .utils import get_city_coordinates


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    # Переопределяем метод create, чтобы добавить координаты
    def create(self, request, *args, **kwargs):
        """ Добавление нового города с координатами. """
        city_name = request.data.get("name")
        if not city_name:
            return Response({"error": "City name is required"},
                            status=status.HTTP_400_BAD_REQUEST)

        coordinates = get_city_coordinates(city_name)
        if not coordinates:
            return Response({"error": "Could not fetch coordinates"},
                            status=status.HTTP_400_BAD_REQUEST)

        # Создаём город с координатами
        city, created = City.objects.get_or_create(
            name=city_name,
            defaults={"latitude": coordinates[0], "longitude": coordinates[1]}
        )
        serializer = self.get_serializer(city)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def nearest(self, request):
        """ Возвращает 2 ближайших города по координатам. """
        latitude = request.query_params.get("latitude")
        longitude = request.query_params.get("longitude")

        if not latitude or not longitude:
            return Response({"error": "Latitude and Longitude are required"},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            latitude, longitude = float(latitude), float(longitude)
        except ValueError:
            return Response({"error": "Invalid coordinates"},
                            status=status.HTTP_400_BAD_REQUEST)

        cities = City.objects.annotate(
            distance=ExpressionWrapper(
                (F("latitude") - latitude) ** 2 +
                (F("longitude") - longitude) ** 2,
                output_field=FloatField(),
            )
        ).order_by("distance")[:2]

        serializer = self.get_serializer(cities, many=True)
        return Response(serializer.data)

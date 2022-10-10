from rest_framework import viewsets

from users.models import Location
from users.serializers.location_serializers import LocationSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

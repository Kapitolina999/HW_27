import json

from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from ads.permissions import OwnerOrStaffPermission
from users.models import Location
from users.serializers.location_serializers import LocationSerializer


# class LocationViewSet(viewsets.ModelViewSet):
#     queryset = Location.objects.all()
#     serializer_class = LocationSerializer


@api_view(['GET'])
def locations(request):
    locations = Location.objects.all()
    return JsonResponse([
            {'name': location.name,
             'lat': location.lat,
             'lng': location.lng} for location in locations], safe=False, json_dumps_params={'ensure_ascii': False})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def location_create(request):
    data = json.loads(request.body)
    location = Location(name=data['name'], lat=data['lat'], lng=data['lng'])
    location.save()
    # return JsonResponse(data, status=200)
    return JsonResponse({'name': location.name, 'lat': location.lat, 'lng': location.lng}, status=201)


@api_view(['GET'])
def location_detail(request, pk):
    try:
        location = Location.objects.get(pk=pk)
    except Location.DoesNotExist:
        return JsonResponse({'error': "Not Found"})
    return JsonResponse(
        {'name': location.name,
         'lat': location.lat,
         'lng': location.lng}, json_dumps_params={'ensure_ascii': False})


@api_view(['DELETE'])
@permission_classes([IsAuthenticated, OwnerOrStaffPermission])
def location_delete(request, pk):
    try:
        location = Location.objects.get(pk=pk)
    except Location.DoesNotExist:
        return JsonResponse({'error': "Not Found"})
    location.delete()
    return JsonResponse(
        {'name': location.name,
         'lat': location.lat,
         'lng': location.lng}, json_dumps_params={'ensure_ascii': False})


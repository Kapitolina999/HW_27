from django.db.models import Q
from rest_framework import viewsets
from ads.models import Ad
from ads.serializers.ad_serializers import AdListSerializer


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdListSerializer

    def get(self, request, *args, **kwargs):
        search_category = request.GET.getlist('cat')
        search_text = request.GET.get('text')
        search_location = request.GET.get('location')
        search_price_min = request.GET.get('price_from')
        search_price_max = request.GET.get('price_to')

        self.queryset = self.queryset.filter(category__in=search_category) if search_category else self.queryset
        self.queryset = self.queryset.filter(name__icontains=search_text) if search_text else self.queryset
        self.queryset = self.queryset.filter(author__locations__name__icontains=search_location) \
            if search_location else self.queryset
        self.queryset = self.queryset.filter(Q(price__gte=search_price_min) & Q(price__lte=search_price_max)) \
            if search_price_min and search_price_max else self.queryset
        return super().get(request, *args, **kwargs)

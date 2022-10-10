from rest_framework import viewsets

from ads.models import Category
from ads.serializers.cat_serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

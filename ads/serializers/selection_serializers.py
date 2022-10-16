from rest_framework import serializers

from ads.models import Selection
from ads.serializers.ad_serializers import AdSerializer


class SelectionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = ['id', 'name']


class SelectionSerializer(serializers.ModelSerializer):
    items = AdSerializer(many=True)

    class Meta:
        model = Selection
        fields = '__all__'


class SelectionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = '__all__'


class SelectionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = ['name', 'items']
from rest_framework import serializers

from ads.models import Ad, Category
from users.models import User


class AdSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(max_length=60, read_only=True)
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)

    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), write_only=True)
    category_name = serializers.CharField(max_length=50, read_only=True)

    class Meta:
        model = Ad
        exclude = ['id']

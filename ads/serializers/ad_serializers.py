from rest_framework import serializers

from ads.models import Ad, Category
from users.models import User


class AdSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(max_length=60, read_only=True)
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True, required=False)

    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), write_only=True, required=False)
    category_name = serializers.CharField(max_length=50, read_only=True)

    def create(self, validated_data):
        if validated_data['is_published']:
            raise serializers.ValidationError('is_published cannot be "True"')
        return super().create(validated_data)

    class Meta:
        model = Ad
        fields = '__all__'

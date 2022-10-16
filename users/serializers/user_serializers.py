from rest_framework import serializers

from users.models import User, Location
from users.serializers.location_serializers import LocationSerializer


class UserListSerializer(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(read_only=True, slug_field='name', many=True)

    class Meta:
        model = User
        exclude = ['id', 'password']


class UserDetailSerializer(serializers.ModelSerializer):
    open_ads = serializers.IntegerField()
    locations = serializers.SlugRelatedField(read_only=True, many=True, slug_field='name')

    class Meta:
        model = User
        exclude = ['password']


class UserCreateSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(many=True, required=False, queryset=Location.objects.all(),
                                            slug_field='name')
    password = serializers.CharField(max_length=128, write_only=True)
    role = serializers.CharField(max_length=9, write_only=True)

    class Meta:
        model = User
        fields = "__all__"

    def is_valid(self, *, raise_exception=False):
        self._location = self.initial_data.pop('location')
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)

        for location in self._location:
            location_object, _ = Location.objects.get_or_create(name=location)
            user.location.add(location_object)

        user.set_password(user.password)

        user.save()
        return user


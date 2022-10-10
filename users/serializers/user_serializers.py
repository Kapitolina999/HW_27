from rest_framework import serializers

from users.models import User, Location


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
    locations = serializers.SlugRelatedField(many=True, required=False, queryset=Location.objects.all(),
                                             slug_field='name')
    password = serializers.CharField(max_length=20, write_only=True)
    role = serializers.CharField(max_length=20, write_only=True)

    class Meta:
        model = User
        exclude = ['id']

    def is_valid(self, *, raise_exception=False):
        self._locations = self.initial_data.pop('locations')
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)

        for location in self._locations:
            location_object, _ = Location.objects.get_or_create(name=location)
            user.locations.add(location_object)

        user.save()
        return user


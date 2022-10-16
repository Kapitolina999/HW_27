from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView

from users.models import User
from users.serializers.user_serializers import UserListSerializer, UserDetailSerializer, UserCreateSerializer


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

    
class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

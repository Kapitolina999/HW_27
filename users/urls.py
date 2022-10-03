from django.urls import path

from users.views import UserListView, UserDetailView, UserCreateView, UserUpdateView, UserDeleteView

urlpatterns = [
    path('', UserListView.as_view(), name='users'),
    path('<int:pk>/', UserDetailView.as_view(), name='user'),
    path('create/', UserCreateView.as_view(), name='user_create'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
]

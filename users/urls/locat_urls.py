from django.urls import path

from users.view.location_views import locations, location_create, location_detail, location_delete

urlpatterns = [
    path('', locations),
    path('create/', location_create),
    path('<int:pk>/', location_detail),
    path('<int:pk>/delete/', location_delete),
    # path('create/', SelectionCreateView.as_view()),
    # path('<int:pk>/update/', SelectionUpdateView.as_view()),
    # path('<int:pk>/delete/', SelectionDeleteView.as_view()),
]
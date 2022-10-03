from django.urls import path

from ads.views.ad_views import AdListView, AdDetailView, AdCreateView, AdUploadImageView, AdUpdateView, AdDeleteView

urlpatterns = [
    path('', AdListView.as_view(), name='ads'),
    path('<int:pk>/', AdDetailView.as_view(), name='ad'),
    path('create/', AdCreateView.as_view(), name='ad_create'),
    path('<int:pk>/upload_image/', AdUploadImageView.as_view(), name='ad_image_upload'),
    path('<int:pk>/update/', AdUpdateView.as_view(), name='ad_update'),
    path('<int:pk>/delete/', AdDeleteView.as_view(), name='ad_delete'),

]



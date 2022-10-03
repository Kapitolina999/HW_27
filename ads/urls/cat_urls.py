from django.urls import path

from ads.views.cat_views import CategoryCreateView, CategoryDetailView, CategoryListView, CategoryUpdateView, \
    CategoryDeleteView

urlpatterns = [
    path('', CategoryListView.as_view(), name='categories'),
    path('<int:pk>/', CategoryDetailView.as_view(), name='category'),
    path('create/', CategoryCreateView.as_view(), name='category_create'),
    path('<int:pk>/update/', CategoryUpdateView.as_view(), name='category_update'),
    path('<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
]

import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from ads.models import Category


class CategoryListView(ListView):
    model = Category

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        return JsonResponse([{'id': category.id, 'name': category.name} for category in self.object_list],
                            safe=False, json_dumps_params={'ensure_ascii': False}, status=200)


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        try:
            category = self.get_object()
        except Category.DoesNotExist:
            return JsonResponse({'error': "Not Found"}, status=404)

        return JsonResponse({'id': category.id, 'name': category.name},
                            json_dumps_params={'ensure_ascii': False}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class CategoryCreateView(CreateView):
    model = Category
    fields = ['name']

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        category_data = json.loads(request.body)
        category = Category.objects.create(name=category_data['name'])

        return JsonResponse({'id': category.id, 'name': category.name}, json_dumps_params={'ensure_ascii': False})


@method_decorator(csrf_exempt, name='dispatch')
class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name']

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        category_data = json.loads(request.body)
        self.object.name = category_data['name']

        return JsonResponse({'id': self.object.id, 'name': self.object.name},
                            json_dumps_params={'ensure_ascii': False})


@method_decorator(csrf_exempt, name='dispatch')
class CategoryDeleteView(DeleteView):
    model = Category
    success_url = 'cat/'

    def delete(self, request, *args, **kwargs):
        return JsonResponse({'status': 'Ok'},
                            json_dumps_params={'ensure_ascii': False}, status=204)

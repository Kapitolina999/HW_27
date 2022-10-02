import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView

from ads.models import Ad, Category


class MainView(View):
    def get(self, request):
        return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class AdView(ListView):
    model = Ad
    def get(self, request):
        ads = self.get_queryset()
        return JsonResponse([
            {'name': ad.name,
             'author': ad.author,
             'price': ad.price,
             'description': ad.description,
             'address': ad.address,
             'is_published': ad.is_published} for ad in ads], safe=False, json_dumps_params={'ensure_ascii': False})

    def post(self, request):
        new_ad = json.loads(request.body)
        ad = Ad(name=new_ad['name'], author=new_ad['author'], price=new_ad['price'], description=new_ad['description'],
                address=new_ad['address'], is_published=new_ad.get('is_published', True))
        ad.save()
        return JsonResponse(new_ad, status=200)


class AdDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        ad = self.get_object()
        return JsonResponse(
            {'name': ad.name,
             'author': ad.author,
             'price': ad.price,
             'description': ad.description,
             'address': ad.address,
             'is_published': ad.is_published}, json_dumps_params={'ensure_ascii': False})


@method_decorator(csrf_exempt, name='dispatch')
class CategoryView(View):
    def get(self, request):
        categories = Category.objects.all()
        return JsonResponse([
            {'name': category.name} for category in categories], safe=False, json_dumps_params={'ensure_ascii': False})

    def post(self, request):
        new_category = json.loads(request.body)
        category = Category(name=new_category['name'])
        category.save()
        return JsonResponse(new_category, status=200)


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        try:
            category = self.get_object()
        except Category.DoesNotExist:
            return JsonResponse({'error': "Нет найдено"}, status=404)

        return JsonResponse({'name': category.name}, json_dumps_params={'ensure_ascii': False})



import json

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from HW_27 import settings
from ads.models import Ad, Category
from users.models import User


class AdListView(ListView):
    model = Ad

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        search_category = request.GET.get('cat')
        status = request.GET.get('status')

        if search_category:
            self.object_list = self.object_list.filter(category=search_category)
        if status:
            self.object_list = self.object_list.filter(is_published=status)

        self.object_list = self.object_list.order_by('-price')
        total_ads = self.object_list.count()
        paginator = Paginator(object_list=self.object_list, per_page=settings.TOTAL_ON_PAGE)
        page = request.GET.get('page')
        page_objects = paginator.get_page(page)
        response = map(lambda ad:
                       {"id": ad.id,
                        "name": ad.name,
                        "author_id": ad.author.id,
                        "author": ad.author.first_name,
                        "price": ad.price,
                        "description": ad.description,
                        "is_published": ad.is_published,
                        "category": ad.category.name,
                        "image": ad.image.url if ad.image else None,
                        "create": ad.created}, page_objects)

        return JsonResponse({'items': list(response), 'total': total_ads, 'num_page': page},
                            json_dumps_params={'ensure_ascii': False}, status=200)


class AdDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        ad = self.get_object()
        return JsonResponse({'id': ad.id,
                             'name': ad.name,
                             'author_id': ad.author.id,
                             'author': ad.author.first_name,
                             'price': ad.price,
                             'description': ad.description,
                             'is_published': ad.is_published,
                             'category': ad.category.name,
                             'image': ad.image.url if ad.image else None,
                             'create': ad.created}, json_dumps_params={'ensure_ascii': False})


@method_decorator(csrf_exempt, name='dispatch')
class AdCreateView(CreateView):
    model = Ad
    fields = ['name', 'author', 'price', 'description', 'is_published', 'category', 'create']

    def post(self, request, *args, **kwargs):
        ad_data = json.loads(request.body)
        author = get_object_or_404(User, id=ad_data['author'])
        category = get_object_or_404(Category, id=ad_data['category'])

        ad = Ad.objects.create(name=ad_data['name'], author=author, price=ad_data['price'],
                               description=ad_data['description'], is_published=ad_data['is_published'],
                               category=category)

        return JsonResponse({"id": ad.id,
                             "name": ad.name,
                             "author_id": ad.author.id,
                             "author": ad.author.first_name,
                             "price": ad.price,
                             "description": ad.description,
                             "is_published": ad.is_published,
                             "category": ad.category.name,
                             "create": ad.created,
                             }, json_dumps_params={'ensure_ascii': False})


@method_decorator(csrf_exempt, name='dispatch')
class AdUpdateView(UpdateView):
    model = Ad
    fields = ['name', 'price', 'description', 'is_published', 'category']

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        ad = self.object()
        ad_data = json.loads(request.body)

        ad.name = ad_data['name']
        ad.price = ad_data['price']
        ad.description = ad_data['description']
        ad.is_published = ad_data['is_published']
        ad.category = get_object_or_404(Category, id=ad_data['category'])
        ad.save()

        return JsonResponse({"id": ad.id,
                             "name": ad.name,
                             "author_id": ad.author.id,
                             "author": ad.author.first_name,
                             "price": ad.price,
                             "description": ad.description,
                             "is_published": ad.is_published,
                             "category": ad.category.name,
                             "create": ad.created,
                             }, json_dumps_params={'ensure_ascii': False})


@method_decorator(csrf_exempt, name='dispatch')
class AdUploadImageView(UpdateView):
    model = Ad
    fields = ['image']

    def post(self, request, *args, **kwargs):
        ad = self.get_object()
        ad.image = request.FILES['image']
        ad.save()
        return JsonResponse({'id': ad.id,
                             'name': ad.name,
                             'author_id': ad.author.id,
                             'author': ad.author.first_name,
                             'price': ad.price,
                             'description': ad.description,
                             'is_published': ad.is_published,
                             'category': ad.category.name,
                             'image': ad.image.url if ad.image else None,
                             'create': ad.created}, json_dumps_params={'ensure_ascii': False})

        # return redirect(url(name=ad))


@method_decorator(csrf_exempt, name='dispatch')
class AdDeleteView(DeleteView):
    model = Ad
    success_url = 'ad/'

    def delete(self, request, *args, **kwargs):
        return JsonResponse({'status': 'Ok'},
                            json_dumps_params={'ensure_ascii': False}, status=204)

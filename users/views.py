import json

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from HW_27 import settings
from users.models import User, Location


class UserListView(ListView):
    model = User

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        self.object_list = self.object_list.order_by('username')
        total_users = self.object_list.count()
        paginator = Paginator(object_list=self.object_list, per_page=settings.TOTAL_ON_PAGE)
        page = request.GET.get('page')
        page_objects = paginator.get_page(page)
        response = map(lambda user:
                       {"id": user.id,
                        "username": user.username,
                        "first_name": user.first_name,
                        "last_name": user.last_name,
                        "role": user.role,
                        "age": user.age,
                        "locations": list(user.location.all().values_list('name', flat=True))}, page_objects)

        return JsonResponse({'items': list(response), 'total': total_users, 'num_page': page},
                            json_dumps_params={'ensure_ascii': False})
    
    
class UserDetailView(DetailView):
    model = User
    
    def get(self, request, *args, **kwargs):
        try:
            user = self.get_object()
        except User.DoesNotExist:
            return JsonResponse({'error': 'user not found'}, status=404)

        open_ads = user.ads.filter(is_published=True).count()
        return JsonResponse({"id": user.id,
                             "username": user.username,
                             "first_name": user.first_name,
                             "last_name": user.last_name,
                             "role": user.role,
                             "age": user.age,
                             "locations": list(user.location.all().values_list('name', flat=True)),
                             'open_ads': open_ads},
                            json_dumps_params={'ensure_ascii': False}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class UserCreateView(CreateView):
    model = User
    fields = ['first_name', 'last_name', 'username', 'password', 'role', 'age', 'location']

    def post(self, request, *args, **kwargs):
        user_data = json.loads(request.body)

        user = User.objects.create(first_name=user_data['first_name'],
                                   last_name=user_data['last_name'],
                                   username=user_data['username'],
                                   password=user_data['password'],
                                   role=user_data['role'],
                                   age=user_data['age'],
                                   )

        for location in user_data['locations']:
            location, _ = Location.objects.get_or_create(name=location)
            user.location.add(location)

        return JsonResponse({"id": user.id,
                             "username": user.username,
                             "first_name": user.first_name,
                             "last_name": user.last_name,
                             "role": user.role,
                             "age": user.age,
                             "location": list(user.location.all().values_list('name', flat=True))},
                            json_dumps_params={'ensure_ascii': False}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'password', 'username', 'age', 'location']

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        user_data = json.loads(request.body)


        self.object.first_name = user_data['first_name']
        self.object.username = user_data['username']
        self.object.last_name = user_data['last_name']
        self.object.password = user_data['password']
        self.object.age = user_data['age']

        for location in user_data['locations']:
            location, _ = Location.objects.get_or_create(name=location)
            self.object.location.add(location)

        return JsonResponse({"id": self.object.id,
                             "username": self.object.username,
                             "first_name": self.object.first_name,
                             "last_name": self.object.last_name,
                             "age": self.object.age,
                             "locations": list(self.object.location.all().values_list('name', flat=True))},
                            json_dumps_params={'ensure_ascii': False}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class UserDeleteView(DeleteView):
    model = User
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return JsonResponse({"status": "ok"}, status=204)

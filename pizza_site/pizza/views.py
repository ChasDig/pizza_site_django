from django.shortcuts import render
from django.http import JsonResponse

from django.views.generic import *
from django.views.generic.list import *

from django.db.models import Q, Max

from .models import *


# Вывод информации о пицце через JsonResponse:
class AllPizzaView(ListView):
    """ Контроллер-класс для работы с моделью 'Pizza':
            - Выводит список пицц
    """

    model = Pizza

    def get(self, request, *args, **kwargs):

        super().get(request, *args, **kwargs)

        pizza_data = []

        # pizza_filter_price = self.request.GET.get('price_filter_max', None)

        if self.request.GET.get('price_filter'):
            self.object_list = self.object_list.filter(price=self.request.GET.get('price_filter'))
        if self.request.GET.get('price_filter_max'):
            self.object_list = self.object_list.filter(Q(price__gte=self.request.GET.get('price_filter_max')))
        if self.request.GET.get('price_filter_min'):
            self.object_list = self.object_list.filter(Q(price__lte=self.request.GET.get('price_filter_min')))

        for pizza_one_daya in self.object_list:
            pizza_data.append({
                'name': pizza_one_daya.name,
                'weight': pizza_one_daya.weight,
                'descriptions': pizza_one_daya.descriptions,
                'price': pizza_one_daya.price,

            })

            response = {'pizza': pizza_data}

        return JsonResponse(response, safe=False)

# Вывод информации о пицце на шаблон:
# class AllPizzaView(ListView):
#
#     model = Pizza
#     template_name = 'pizza/pizza_list.html'
#     context_object_name = 'pizza'
#
#     def get_context_data(self, *args, **kwargs):
#
#         context = super().get_context_data(*args, **kwargs)
#
#         return context



class SearchPizzaView(ListView):
    """ Контроллер-класс для работы с диспетчером записи модели 'Pizza':
            - Фильтрует пиццы для их поиска
    """

    context_object_name = 'pizza'

    def get_queryset(self):
        return Pizza.objects.filter(name__icontains=self.request.GET.get('query'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = f"query={self.request.GET.get('query')}&"

        return context


class OrderPizzaView(ListView):
    pass

from django.urls import path, include

from .views import *

# Создаем views для нашего приложения:
urlpatterns = [
    path('', AllPizzaView.as_view(), name='pizza_view'),
    path('search_pizza', SearchPizzaView.as_view(), name='search_pizza'),
]

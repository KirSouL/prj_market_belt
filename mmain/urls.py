from django.urls import path
from mmain.views import index, login, catalog, basket

urlpatterns = [
    path('', index, name='home'),
    path('login/', login, name='login'),
    path('catalog/', catalog, name='catalog'),
    path('basket/', basket, name='basket'),
]
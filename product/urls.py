from unicodedata import name
from django.urls import path
from .views import list_products, create_product, update, hijo1, hijo2

urlpatterns = [
    path('', list_products, name='listar_productos'),
    path('crear/', create_product, name="crear_producto"),
    path('editar/{id}', update, name='editar'),
    path('hijo1/', hijo1),
    path('hijo2/', hijo2),
]

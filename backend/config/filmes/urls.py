from django.urls import path
from . import views

urlpatterns = [
    path("", views.listar, name="listar"),
    path("cadastrar/", views.cadastrar, name="cadastrar"),
    path("filme/<int:pk>/", views.detalhe, name="detalhe"),
    path("filme/<int:pk>/editar/", views.editar, name="editar"),
    path("filme/<int:pk>/excluir/", views.excluir, name="excluir"),
    path("buscar/", views.buscar, name="buscar"),
]
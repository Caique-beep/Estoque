"""estoque URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from controle import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.vwProdutos, name='vwProdutos'),
    path('produtosEdit/<int:pk>/', views.produtos_edit, name='produtosEdit'),
    path('produtosAdd/', views.produtos_add, name='produtosAdd'),
    path('prod_del/<int:pk>/', views.produtos_del, name='produtosDel'),
    path('Estoque/', views.estoque, name='vwEstoque'),
    path('Entrada/', views.vwEntradas, name='vwEntrada'),
    path('nova_entrada/', views.nova_entrada, name='nova_entrada'),
    path('entradaEdit/<int:pk>/', views.entrada_edit, name='entradaEdit'),
    path('ent_del/<int:pk>/', views.entrada_del, name='entradaDel'),
    path('Saida/', views.vwSaidas, name='vwSaida'),
    path('nova_saida/', views.nova_saida, name='nova_saida'),
    path('saidaEdit/<int:pk>/', views.saida_edit, name='saidaEdit'),
    path('saida_del/<int:pk>/', views.saida_del, name='saida_del'),
    path('searchbar/', views.searchbar, name='searchbar'),
]

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
    path('Estoque/', views.estoque, name='estoque'),
]
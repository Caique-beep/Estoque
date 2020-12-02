from django.urls import path
from entrada import views


urlpatterns = [
    path('', views.vwEntradas, name='vwEntrada'),
    path('nova_entrada/', views.nova_entrada, name='nova_entrada'),
    path('entradaEdit/<int:pk>/', views.entrada_edit, name='entradaEdit'),
    path('ent_del/<int:pk>/', views.entrada_del, name='entradaDel'),
    path('searchBarEnt/', views.search_bar_ent, name='searchBarEnt'),
]
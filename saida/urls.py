from django.urls import path
from saida import views


urlpatterns = [
    path('', views.vwSaidas, name='vwSaida'),
    path('nova_saida/', views.nova_saida, name='nova_saida'),
    path('saidaEdit/<int:pk>/', views.saida_edit, name='saidaEdit'),
    path('saida_del/<int:pk>/', views.saida_del, name='saida_del'),
]

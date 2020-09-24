from django.contrib import admin
from .models import Produtos, Estoque

admin.site.register(Estoque)
admin.site.register(Produtos)


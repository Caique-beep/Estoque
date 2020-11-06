from django.contrib.auth.forms import forms
from .models import Produtos, Entrada


class ProdutosForm(forms.ModelForm):
    descricao = forms.CharField(max_length=20)
    custo = forms.DecimalField(max_digits=5, decimal_places=2)
    preco = forms.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        model = Produtos
        fields = ['descricao', 'custo', 'preco']


class EntradasForm(forms.ModelForm):

    quantidade = forms.IntegerField(max_value=None)

    class Meta:
        model = Entrada
        fields = [ 'quantidade', 'descricao']



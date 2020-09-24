from django.shortcuts import render, redirect
from .forms import ProdutosForm
from .models import Produtos, Estoque


def vwProdutos(request):
    data = {}
    produtoModel = Produtos.objects.all()
    data['produtos'] = produtoModel
    return render(request, "controle/vwProdutos.html", data)


def produtos_add(request):
    data = {}
    if request.method == 'POST':
        prod_form = ProdutosForm(request.POST)

        if prod_form.is_valid():
            produtos = prod_form.save(commit=False)
            produtos.save()

            est_form = Estoque(produto=produtos,entradas = 0, saidas= 0, balanco=0, custo_estimado=0,venda_esperada=0)
            print(est_form.custo_estimado, 'Custp')
            est_form.save()
            print(est_form.custo_estimado, 'Custpaaaa')
            return redirect('vwProdutos')

    data['prod_form']= ProdutosForm
    data['est_form'] = Estoque

    return render(request, "controle/produtosAdd.html", data)


def produtos_edit(request, pk):
    data = {}
    prod = Produtos.objects.get(pk=pk)
    form = ProdutosForm(request.POST or None, instance=prod)
    if form.is_valid():
        form.save()
        return redirect('vwProdutos')
    data['produtos'] = prod
    data['form'] = form
    return render(request, 'controle/produtosAdd.html', data)


def produtos_del(request, pk):
    produto_deletar = Produtos.objects.get(pk=pk)
    produto_deletar.delete()
    return redirect('vwProdutos')


def estoque(request):
    est = Estoque.objects.all()
    return render(request, 'controle/vwEstoque.html', {est: 'estoque'})
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProdutosForm, EntradasForm
from .models import Produtos, Estoque, Entrada


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
            est_form = Estoque(produto=produtos, entradas=0, saidas=0,
                               balanco=0, custo_estimado=0, venda_esperada=0)
            est_form.save()
            return redirect('vwProdutos')
    data['prod_form'] = ProdutosForm
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
    data['prod_form'] = form
    return render(request, 'controle/produtosAdd.html', data)


def produtos_del(request, pk):
    produto_deletar = Produtos.objects.get(pk=pk)
    produto_deletar.delete()
    return redirect('vwProdutos')


def estoque(request):
    data = {}
    est = Estoque.objects.all()
    data['estoque'] = est
    return render(request, 'controle/vwEstoque.html', data)


def vwEntradas(request):
    data = {}
    ent = Entrada.objects.all()
    data['entradas'] = ent
    return render(request, 'controle/vwEntradas.html', data)


def nova_entrada(request):
    data = {}
    form = EntradasForm(request.POST or None)
    prod = Produtos.objects.all()
    if request.method == 'POST':
        post = form.save(commit=False)
        selected_item = get_object_or_404(prod, descricao=request.POST.get('descricao'))
        post.descricao = selected_item
        prd = Produtos.objects.get(descricao=selected_item)
        print(prd.id)
        post.codigo_id = prd.id
        post.save()


        est = Estoque.objects.get(pk=prd.id)
        est.entradas = est.entradas + post.quantidade
        est.save()
        return redirect('vwEntrada')
    data['prod'] = prod
    data['entrada'] = form
    return render(request, 'controle/nova_entrada.html', data)


def entrada_edit(request, pk):
    data = {}
    ent = Entrada.objects.get(pk=pk)
    form = EntradasForm(request.POST or None, instance=ent)
    prod = Produtos.objects.all()
    if request.method == 'POST':
        post = form.save(commit=False)
        selected_item = get_object_or_404(prod, descricao=request.POST.get('descricao'))
        post.descricao = str(selected_item)
        post.save()
        return redirect('vwEntrada')
    data['prod'] = prod
    data['entrada'] = form
    return render(request, 'controle/nova_entrada.html', data)


def entrada_del(request, pk):
    produto_deletar = Entrada.objects.get(pk=pk)
    produto_deletar.delete()
    return redirect('vwEntrada')

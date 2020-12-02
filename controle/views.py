from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProdutosForm, EntradasForm, SaidasForm
from .models import Produtos, Estoque, Entrada, Saida
from decimal import Decimal


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
            est_form.pk = produtos.id
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
        est = Estoque.objects.get(pk=prod.id)
        cust_est = Decimal(est.balanco) * Decimal(prod.custo)
        est.custo_estimado = cust_est
        prc = Decimal(est.balanco) * Decimal(prod.preco)
        est.venda_esperada = prc
        est.save()
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













def att_estoque(val_id, prd, chave):
    est = Estoque.objects.get(pk=val_id)
    if chave:
        ent = Entrada.objects.filter(codigo_id=val_id).values('quantidade')
        est.entradas = sum([i['quantidade'] for i in ent])

    else:
        ent = Saida.objects.filter(codigo_id=val_id).values('quantidade')
        est.saidas = sum([i['quantidade'] for i in ent])
    est.balanco = est.entradas - est.saidas
    cust_est = Decimal(est.balanco) * Decimal(prd.custo)
    est.custo_estimado = cust_est
    prc = Decimal(est.balanco) * Decimal(prd.preco)
    est.venda_esperada = prc
    est.save()



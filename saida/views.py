from django.shortcuts import render, get_object_or_404, redirect
from controle.models import Saida, Produtos
from controle.forms import SaidasForm
from controle.views import att_estoque


def vwSaidas(request):
    data = {}
    saida = Saida.objects.all()
    data['saidas'] = saida
    return render(request, 'saida/vwSaidas.html', data)


def nova_saida(request):
    data = {}
    form = SaidasForm(request.POST or None)
    prod = Produtos.objects.all()
    if request.method == 'POST':
        post = form.save(commit=False)
        selected_item = get_object_or_404(prod, descricao=request.POST.get('descricao'))
        post.descricao = selected_item
        prd = Produtos.objects.get(descricao=selected_item)
        post.codigo_id = prd.id
        post.save()

        att_estoque(prd.id, prd, False)

        return redirect('vwSaida')
    data['prod'] = prod
    data['saida'] = form
    return render(request, 'saida/nova_saida.html', data)


def saida_edit(request, pk):
    data = {}
    sd = Saida.objects.get(pk=pk)
    form = SaidasForm(request.POST or None, instance=sd)
    prod = Produtos.objects.all()
    if request.method == 'POST':
        post = form.save(commit=False)
        selected_item = get_object_or_404(prod, descricao=request.POST.get('descricao'))
        post.descricao = str(selected_item)
        prd = Produtos.objects.get(descricao=selected_item)
        post.codigo_id = prd.id
        post.save()

        att_estoque(prd.id, prd, False)

        return redirect('vwSaida')
    data['prod'] = prod
    data['saida'] = form
    return render(request, 'saidanova_saida.html', data)


def saida_del(request, pk):
    saida_deletar = Saida.objects.get(pk=pk)
    saida_deletar.delete()
    return redirect('vwSaida')
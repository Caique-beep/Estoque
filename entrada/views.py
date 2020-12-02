from django.shortcuts import render, get_object_or_404, redirect
from controle.models import Entrada, Produtos
from controle.forms import EntradasForm
from controle.views import att_estoque


def vwEntradas(request):
    data = {}
    ent = Entrada.objects.all()
    data['entradas'] = ent
    return render(request, 'entrada/vwEntradas.html', data)


def nova_entrada(request):
    data = {}
    form = EntradasForm(request.POST or None)
    prod = Produtos.objects.all()
    if request.method == 'POST':
        post = form.save(commit=False)
        selected_item = get_object_or_404(prod, descricao=request.POST.get('descricao'))
        post.descricao = selected_item
        prd = Produtos.objects.get(descricao=selected_item)
        post.codigo_id = prd.id
        post.save()

        att_estoque(prd.id, prd, True)
        return redirect('vwEntrada')
    data['prod'] = prod
    data['entrada'] = form
    return render(request, 'entrada/nova_entrada.html', data)


def entrada_edit(request, pk):
    data = {}
    ent = Entrada.objects.get(pk=pk)
    form = EntradasForm(request.POST or None, instance=ent)
    prod = Produtos.objects.all()
    if request.method == 'POST':
        post = form.save(commit=False)
        selected_item = get_object_or_404(prod, descricao=request.POST.get('descricao'))
        post.descricao = str(selected_item)
        prd = Produtos.objects.get(descricao=selected_item)
        post.codigo_id = prd.id
        post.save()

        att_estoque(prd.id, prd, True)

        return redirect('vwEntrada')
    data['prod'] = prod
    data['entrada'] = form
    return render(request, 'entrada/nova_entrada.html', data)


def entrada_del(request, pk):
    produto_deletar = Entrada.objects.get(pk=pk)
    produto_deletar.delete()
    return redirect('vwEntrada')


def search_bar_ent(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        post = Entrada.objects.all().filter(descricao=search)
        return render(request, 'entrada/searchBarEnt.html', {'post':post})
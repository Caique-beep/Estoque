from django.db import models


class Produtos(models.Model):

    descricao = models.CharField(max_length=50)
    custo = models.DecimalField(
        'Custo',
        max_digits=5,
        decimal_places=2
    )
    preco = models.DecimalField(
        'Preço de Venda',
        max_digits=5,
        decimal_places=2
    )

    def __str__(self):
        return self.descricao


class Entrada(models.Model):
    codigo = models.ForeignKey(Produtos, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=50)
    quantidade = models.IntegerField('Quantidade')
    data = models.DateField(auto_now=True)


class Saida(models.Model):
    codigo = models.ForeignKey(Produtos, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=50)
    quantidade = models.IntegerField('Quantidade')
    data = models.DateField(auto_now=True)


class Estoque(models.Model):
    produto = models.ForeignKey(Produtos, on_delete=models.CASCADE)
    entradas = models.IntegerField('Entradas', default=0)
    saidas = models.IntegerField('Saidas', default=0)
    balanco = models.IntegerField('Balanço', default=0)
    custo_estimado = models.DecimalField(
        'Custo estimado',
        max_digits=5,
        decimal_places=2,
        default=0.00
    )

    venda_esperada = models.DecimalField(
        'Venda Esperada',
        max_digits=5,
        decimal_places=2
    )

    def __str__(self):
        return self.produto.descricao

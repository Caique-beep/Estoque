from django.test import TestCase
from controle.models import Produtos, Entrada
# Create your tests here.


class TestModelProdutos(TestCase):
    def setUp(self) -> None:
        self.produto = Produtos(codigo='001', descricao='livro', custo= '10,00', preco= '20,00')

    def test_produto_deve_retonar_seu_codigo(self):
        esperado = ('001', 'livro')
        resultado =(self.produto.codigo, self.produto.descricao)

        self.assertEqual(esperado, resultado)


class TestModelEntrada(TestCase):
    def setUp(self) -> None:
        self.produto = Produtos(codigo='001', descricao='livro', custo='10,00', preco='20,00')
        self.entrada = Entrada(codigo=self.produto, descricao= 'livro', quantidade= 10, data='31/08/20')

    def test_model_entrada_deve_salvar(self):
        esperado = ('001', 'livro')
        resultado = (self.entrada.codigo.codigo, self.entrada.descricao)

        self.assertEqual(esperado, resultado)
"""
Agregação/Composição
Uma classe usa outra como parte de si
"""

class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []
        
    def inserirProduto(self, produto):
        self.produtos.append(produto)
    
    def listaProdutos(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)
    
    def somaTotal(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return f'{total:.2f}'.replace('.', ',')

class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
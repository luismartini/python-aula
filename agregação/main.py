from classe import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()
p1 = Produto('Camiseta', 50)
p2 = Produto('iPhone', 15000)
p3 = Produto('Caneca', 15)

carrinho.inserirProduto(p2)
carrinho.inserirProduto(p1)
carrinho.inserirProduto(p3)
carrinho.inserirProduto(p2)
carrinho.inserirProduto(p2)

carrinho.listaProdutos()
print(carrinho.somaTotal())
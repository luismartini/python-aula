carrinho = []
carrinho.append(('Produto 1', 30.50))
carrinho.append(('Produto 1', 10))
carrinho.append(('Produto 1', 20))

total = sum([y for x, y in carrinho])
print(f'O total da compra deu {total}')
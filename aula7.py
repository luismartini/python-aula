#formatação de string

nome = 'Luís'
idade = 44
altura = 1.8456

print(f'{nome} tem {idade} anos de idade e sua altura é de {altura:.2f}')


print('{0} tem {1} anos de idade e sua altura é de {2}'.format(nome, idade, altura))
print('{n} tem {i} anos de idade e sua altura é de {a}'.format(n=nome, i=idade, a=altura))
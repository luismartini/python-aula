'''
while em Python
utilizado para realizar ações enquanto
uma condição for verdadeira
#continue
#break - termina o loop
'''
# i = 0
# while i <= 10:
#     if i == 3:
#         i += 1
#         break
#     print('Contador', i)
#     i += 1

# print('Acabou!')

# x = 0 #coluna
# while x < 10:
#     y = 0 #linha
#     while y < 5:
#         print(f'({x}, {y})')
#         y += 1
#     x += 1
# print('Acabou!')

while True:
    print()
    num1 = input('Digite um número: ')
    num2 = input('Digite outro número: ')
    operador = str(input('Digite um operador: '))
    sair = input('Deseja sair [S/N]')[0]
    
    
    if sair == 's':
        break
    #checar se é número
    # if type(num1) or type(num2) != int:
    #     print('Digite apenas números!')
    
    #Segunda forma de checar
    if not num1.isnumeric() or not num2.isnumeric():
        print('Digite apenas números')
    
    num1 = int(num1)
    num2 = int(num2)
    
    if operador == '+':
        print((num1 + num2))
    elif operador == '-':
        print(num1 - num2)
    elif operador == '/':
        print(num1 / num2)
    elif operador == '*':
        print(num1 * num2)
    elif operador == '%':
        print(num1 % num2)
    else:
        print('Operador inválido')
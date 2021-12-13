'''
1. Crie uma função que exiba uma saudação com os parâmetros saudação e nome
'''
# def saudacao(saudacao, nome):
#     print(f'{saudacao} {nome}')
# saudacao('Olá', 'Luís Martini')

'''
2. Crie uma função que receba 3 números como parâmetros e exiba a soma entre eles. Não pede para retornar.
'''

# def soma(n1, n2, n3):
#     print(n1 + n2 + n3)

# soma(1, 2, 3)
# soma(1,1,1)
# soma(2,1,1)

'''
3. Crie uma função que receba 2 números. O primeiro é um valor e o segundo um percentual (ex. 10%). Retorne (return) o valor do primeiro número somado ao aumento percentual do mesmo.
'''

# def aumentoPercentual(valor, percentual):
#     return valor + (valor * percentual/100)


# ap = aumentoPercentual(50, 10)
# print(ap)
# ap = aumentoPercentual(100, 10)
# print(ap)
# ap = aumentoPercentual(10, 10)
# print(ap)
# ap = aumentoPercentual(15, 100)
# print(ap)


'''
4. Fizz Buzz - Se o parâmetro da função for divisível por 2, retorn fizz, se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da função for divisível por 5 e por 3, retorn FIZZBUZZ, caso contrário, retorne o número enviado.
'''

def executaFizzBuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return f'FizzBuzz, {n} é divisível por 3 e 5'
    if n % 3 == 0:
        return f'Fizz, {n} é divisível por 3'
    if n % 5 == 0:
        return f'Buzz, {n} é divisível por 5'
    return n

print(executaFizzBuzz(7))
print(executaFizzBuzz(10))
print(executaFizzBuzz(15))
print(executaFizzBuzz(22))

from random import randint

for i in range(20):
    aleatorio = randint(0, 20)
    print(executaFizzBuzz(aleatorio))
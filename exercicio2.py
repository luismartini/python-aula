'''
1. Crie uma função que exiba uma saudação com os parâmetros saudação e nome
'''
def saudacao(saudacao='Oi', nome='Luís'):
    print(saudacao, nome)
    
saudacao()

'''
2. Crie uma função que receba 3 números como parâmetros e exiba a soma entre eles. Não pede para retornar.
'''
def soma(n1, n2, n3):
    print(n1 + n2 + n3)
soma(1,2,3)
soma(1,1,1)

'''
3. Crie uma função que receba 2 números. O primeiro é um valor e o segundo um percentual (ex. 10%). Retorne (return) o valor do primeiro número somado ao aumento percentual do mesmo.
'''
def percentual(valor, percentual):
    return valor + (valor * percentual/100)
ap = percentual(100, 30)
print(ap)

'''
4. Fizz Buzz - Se o parâmetro da função for divisível por 2, retorn fizz, se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da função for divisível por 5 e por 3, retorn FIZZBUZZ, caso contrário, retorne o número enviado.
'''
def executaFizzBuzz(n):
    if n % 5 == 0 and n % 3 == 0:
        return 'FizzBuzz'
    if n % 2 == 0:
        return 'Fizz'
    if n % 5 == 0:
        return 'Buzz'
    return n
print(executaFizzBuzz(8))
print(executaFizzBuzz(10))
print(executaFizzBuzz(15))
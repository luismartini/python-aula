'''
Operadores relacionais
< (menor) 
<= (menor igual) 
> (maior) 
>= (maior igual) 
== igualdade 
!= diferente
retorna boolean
'''
nome = input('Qual seu nome? ')
idade = int(input('Qual a sua idade? '))

if 18 <= idade <= 30:
    print(f'{nome} pode pegar o empréstimo!')
else:
    print(f'{nome} não pode pegar o empréstimo')
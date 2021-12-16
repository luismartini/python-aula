perguntas = {
    'Pergunta 1' : {
        'pergunta' : 'Quanto é 2 + 2?',
        'respostas' : {
            'a' : '1',
            'b' : '4',
            'c' : '5',
            'd' : '6',
            'e' : '7',
        },
    'resposta_certa' : 'b'
    },
    'Pergunta 2' : {
        'pergunta' : 'Quanto é 3 * 2',
        'respostas' : {
            'a' : '6',
            'b' : '5',
            'c' : '7',
            'd' : '9',
            'e' : '11',
        },
    'resposta_certa' : 'a'
    },
}
print()
respostas_certas = 0
respostas_erradas = 0
for pk, pv in perguntas.items():
    print(f'{pk} : {pv["pergunta"]}')
    print('Escolha as opções abaixo: ')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')
        
    resposta_usuario = input('Sua resposta é: ')
    
    if resposta_usuario == pv['resposta_certa']:
        print('Você respondeu corretamente')
        respostas_certas += 1
    else:
        print('Tente mais uma vez!')
        respostas_erradas += 1

qtd_perguntas = len(perguntas)
porcentagem_acertos = respostas_certas / qtd_perguntas * 100

print(f'Você acentou {respostas_certas} respostas.')
print(f'Você acertou {porcentagem_acertos}%')

# if porcentagem_acertos == 100:
#     print('Você está bem!')
# elif porcentagem_acertos <= 50:
#     print('Você está mediano')
# else:
#     print('Você precisa estudar mais.')


# if respostas_certas:
#     print(f'Você acertou {respostas_certas}')
# elif respostas_certas or respostas_erradas:
#     print(f'Você acertou {respostas_certas} e errou {respostas_erradas}')
# else:
#     print(f'Você errou {respostas_erradas}')
# print()

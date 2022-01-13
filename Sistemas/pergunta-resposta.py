perguntas = {
    'Pergunta 1' : {
        'pergunta' : 'Quanto é 2/2?',
        'resposta' : {
            'a' : '1',
            'b' : '2',
            'c' : '0,5',
        },
    'resposta_correta' : 'a'
    },
    'Pergunta 2' : {
        'pergunta' : 'Quanto é 4/8',
        'resposta' : {
            'a' : '0,5',
            'b' : '1',
            'c' : 2,
        },
    'resposta_correta' : 'a'
    },
}

respostas_certas = 0
respostas_erradas = 0

for pk, pv in perguntas.items():
    print(f'{pk} : {pv["pergunta"]}')
    print('Escolha as opções abaixo: ')

    for rk, rv in pv['resposta'].items():
        print(f'[{rk}] : {rv}')
    
    resposta_usuario = input('Escolha a resposta correta: ')
    
    if resposta_usuario == pv['resposta_correta']:
        print('Você respondeu corretamente')
        respostas_certas += 1
    else:
        print('Você precisa melhorar')
        respostas_erradas += 1
    
qtd_pergunta = len(perguntas)
porcentagem = respostas_certas / qtd_pergunta * 100
    
print(f'Você acertou {respostas_certas}')
print(f'Conseguiu um total de {porcentagem}%')

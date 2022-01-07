import re
import random


#constante letra maiúscula
REGRESSIVOS = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

def valida(cnpj):
    cnpj = apenas_numeros(cnpj)
    
    if ehsequencia(cnpj):
        return False
    
    try:
        novo_cnpj = calcula_digito(cnpj=cnpj, digito=1)
        novo_cnpj = calcula_digito(cnpj=novo_cnpj, digito=2)
    except Exception as e:
        return False
    
    if novo_cnpj == cnpj:
        return True
    else:
        return False
    
    
def calcula_digito(cnpj, digito):
    if digito == 1:
        regressivos = REGRESSIVOS[1:]
        novo_cnpj = cnpj[:-2]
    elif digito == 2:
        regressivos = REGRESSIVOS
        novo_cnpj = cnpj
    else:
        return None
    
    total = 0
    for indice, regressivo in enumerate(regressivos):
        total += int(cnpj[indice]) * regressivo
    
    digito = 11 - (total % 11)
    digito = digito if digito <= 9 else 0
    #print(digito)
    
    return f'{novo_cnpj}{digito}'
    
def ehsequencia(cnpj):
    sequencia = cnpj[0] * len(cnpj)
    
    if sequencia == cnpj:
        return True
    else:
        False
    
    print(sequencia)

def apenas_numeros(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)

def gera():
    primeiroDigito = random.randint(0, 9)
    segundoDigito = random.randint(0, 9)
    segundoBloco = random.randint(100, 999)
    terceiroBloco = random.randint(100, 999)
    quartoBloco = '0001'
    
    início_cnpj = f'{primeiroDigito}{segundoDigito}{segundoBloco}'\
        f'{terceiroBloco}{quartoBloco}00'
    
    novo_cnpj = calcula_digito(cnpj=início_cnpj, digito=1)
    novo_cnpj = calcula_digito(cnpj=novo_cnpj, digito=2)
    
    return novo_cnpj

def formata(cnpj):
    cnpj = apenas_numeros(cnpj)
    formatado = f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}'
    return formatado
string = '01234567890123456789012345678901234567890123456789'

n = 10                                                  #n pular de n em n/10 em 10
lista = [string[i: i + n] for i in range(0, len(string), n)]  #início, fim, passo
retorno = '.'.join(lista)
print(lista)
print(retorno)
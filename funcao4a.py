variavel = 'valor'

def func():
    outra_variavel = 'valor'
    return outra_variavel

def func2(arg):
    print(arg)
    
var = func()
func2(var)


# def func():
#     print(variavel)

# def func2(arg=None):
#     arg = arg.replace('v', 'c')
#     # variavel = 'Outro valor'  #escopo local
#     # print(variavel)
#     return arg
    
# func()
# outra_variavel = func2(arg=variavel)

# print(outra_variavel)
# def func():
#     print(variavel)
#     variavel = 1234
#     print(variavel)

# func()
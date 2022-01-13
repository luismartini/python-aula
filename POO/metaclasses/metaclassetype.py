A = type(
    'A', 
    (), 
    {
        'attr': 'Olá, Mundo!'
        }
    )
a = A()
print(a.attr)
print(type(a))

help(A)

'''
TYPE é uma metaclasse utilizada para criar classes.
'''
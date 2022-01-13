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


'''
TYPE é uma metaclasse utilizada para criar classes.
'''
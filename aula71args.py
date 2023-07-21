'''
def soma(x, y):
return x+y
'''

#lembrar do desempacotamento
x, y, *resto = 1,2,3,4
print(x,y,resto) #gera uma lista com o restante dos objetos

def soma(*args):
    total = 0
    for numero in args:
        print('Total', total, numero)
        total += numero
        print('Total', total)
    print(total)

soma(1,2,3,4,5,6)

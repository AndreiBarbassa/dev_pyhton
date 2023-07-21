'''
def soma(x, y):
return x+y


args - argumentos nao nomeados
* - args (empacotamento e desempacotamento)
'''

#lembrar do desempacotamento
# x, y, *resto = 1,2,3,4
# print(x,y,resto) #gera uma lista com o restante dos objetos

def soma(*args): #args empacota em tupla
    total = 0
    for numero in args:
        total += numero
    return total

soma_1_2_3 = soma(1, 2, 3)
# print(soma_1_2_3)

soma_4_5_6 = soma(4, 5, 6)
# print(soma_4_5_6)


numeros = 13, 123, 4, 56, 7, 8
outra_soma = soma(*numeros)
print(outra_soma)

print(numeros)
print(*numeros)
print(sum(numeros))

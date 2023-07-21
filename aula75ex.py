# '''
# crie funções que duplicam, triplicam e quadruplicam o
# numero recebido como parâmetro.
# '''

# numero = input('Digite um número:')

# #2x
# def duplicar(numero):
#   return 2*int(numero)

# print(duplicar(numero))


# #3x
# def triplicar(numero):
#   return 3*int(numero)

# print(triplicar(numero))


# #4x
# def quadruplicar(numero):
#   return 4*int(numero)

# print(quadruplicar(numero))

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(8))
print(triplicar(8))
print(quadruplicar(8))
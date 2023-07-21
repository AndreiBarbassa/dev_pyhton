#desempacotamento em chamadas
# de métodos e funções
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

# p, b, *_, pe, u = lista
# print(p, u, pe)

# print('Maria', 'Helena', 1, 2, 3, 'Eduarda')
# print(*lista)
# print(*string)
# # print(*tupla)

salas = [
    ['Maria', 'Helena'],
    ['Elaine'],
    ['Luiz','João','Eduarda'],
    ]

print(*salas, sep='\n', end=' quebrou') #a sequencia de sep e end nao importa.
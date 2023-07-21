"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista = [10, 20, 30, 40]
# lista [2] = 300
# del lista[2]
# print(lista)
# print(lista[2])
lista.append(50)
lista.pop() #remove o ultimo valor da lista
lista.append(60)
lista.append(70)
ultimovalor = lista.pop(3) #para saber qual foi o valor removido
print(lista, 'Removido,', ultimovalor)
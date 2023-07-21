"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista = [10, 20, 30, 40]
print(lista)
lista.append('Andrei')
print(lista)
nome = lista.pop() #ulitmo item adicionado. se 'pop' foi excluido
print(nome)
lista.append(1233)
print(lista)
del lista[-1]
print(lista)
lista.insert(10000,5)
print(lista)
print(type(lista[2]))
lista.clear()
print(lista)
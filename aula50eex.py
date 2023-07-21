'''
Exiba os índices da lista
0 Andrei
1 Nayara
2 Alex
'''
'''
TENTATIVA ANDREI... DEU CERTO MAS NAO É DINÂMICO.

nome1 = "Andrei"
nome2 = "Nayara"
nome3 = "Alex"

lista = ["Andrei","Nayara","Alex"]

for nome in lista:
    if nome == nome1:
        print (0, "Andrei")
    if nome == nome2:
        print(1, "Nayara")
    if nome == nome3:
        print(2,"Alex")

        RESOLUÇÃO: 
'''
lista = ["Andrei","Nayara","Alex"]
indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice])
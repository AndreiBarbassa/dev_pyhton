"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - a
"""
lista_a = ['Andrei', 'Nayara', True, 1.2, 2019]
print(lista_a)

print()

lista_b = lista_a #toda modificação em lista_a alterará lista_b (como se a lista_b apenas apontasse pra lista_a, compartilham os mesmo elementos!)
print(lista_b)

print()

lista_a[0] = 'troquei o nome aqui por qualquer coisa'
print(lista_b) #há alteração no valor de lista b

print()

''' voltando: '''

lista_a = ['Andrei', 'Nayara', True, 1.2, 2019]
lista_b = lista_a.copy() #torna a lista_b independente da lista_a (como se apenas copiasse os elementos da lista e criasse uma nova)

print()

print (lista_b)

print()

lista_a[0] = "troquei em a mas continua em b por conta do .copy"

print()

print (lista_a)
print (lista_b)


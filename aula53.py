lista = ["Andrei","Nayara","Alex"]
lista.append('João')

lista_enumerada = list(enumerate(lista))


#for item in lista_enumerada:
#   print(item)
for indice, nome in lista_enumerada:
    #indice, nome = item dentro la lista (que é uma tupla ex: 0, Andrei)
    print(indice,nome,lista[indice]) #lista[indice] busca o nome daquele indice, não é o próprio indice

'''

for item in enumerate(lista): #aqui os dados estão empacotados, sairão juntos
    print(item)
'''

'''

for tupla_enumerada in enumerate(lista): #desempacotamento de tupla (imprimindo um valor de cada vez)
    print('For da tupla:')
    for valor in tupla_enumerada: #nesse ponto é preciso saber que existem 2 valores dentro de tupla_enumerada (o indice e o nome ex: 0, Andrei)
        print(f'\t{valor}') #\t é o TAB
        
'''

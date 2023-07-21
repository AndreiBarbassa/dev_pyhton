'''
Iterável -> elemento que pode te entregar uma coisa por vez (str, range, etc [___iter___])
Iterador -> quem sabe entregar um valor por vez
next -> me entraga o proximo valor
iter -> me entrega seu iterador
'''

#texto = 'Luiz'.__iter__()
'''é igual a: '''
# texto = iter('Luiz') #__iter__()

# print (texto.__next__())
# print (texto.__next__())
# print (texto.__next__())
# print (texto.__next__())
# print (texto.__next__())

texto = 'Luiz' #iterável
# iterador = iter(texto) #iterator

# while True:
#     try:
#         letra = next(iterador)
#         print(letra)
#     except StopIteration:
#         break
''' acima é a descrição, o detalhamento do que a função
for faz'''

for letra in texto:
    print(letra)
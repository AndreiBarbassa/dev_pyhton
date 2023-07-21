'''
Introdução ao desempacotamento
'''
#primeira maneira
lista = ["Andrei","Nayara","Alex"]
nome1, nome2, nome3 = lista
print(nome1)

#segunda maneira
nome1, nome2, nome3 = ["Andrei","Nayara","Alex"]
print(nome2)
#para a mesma quantidade de variáveis e valores

#terceira maneira
nome1, *resto = ["Andrei","Nayara","Alex"]
print(nome1, resto)

#por convenção, quando nao se usará uma varável utiliza um '_'
nome1, *_ = ["Andrei","Nayara","Alex"]
print(nome1)

_, _, nome, *resto = ["Andrei","Nayara","Alex"]
print(nome)
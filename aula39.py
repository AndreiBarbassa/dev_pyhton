'''
Iterando strings com while
'''
#       012345
'''
nome = 'Andrei' #interáveis
#       654321
tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)

print(nome[2])
'''

nome = 'Andrei'

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)
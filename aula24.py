# Operadores in e not in
# Strings são iteráveis (navegável item por item)
#  0 1 2 3 4 5 (indice positivo de OTAVIO)
#  O t á v i o
# -6-5-4-3-2-1 (indice negativo de OTAVIO)
nome = 'Otávio'
#print(nome [2]) #retorna a letra á (positivo)
#print(nome [-4]) #retorna a letra á (negativo)
#print('á' in nome) #condição: se verdade retorna true
#print('z' in nome) #condição falsa
#print('vio' in nome) 
#print('and' in nome)
#print('vio' not in nome) #falso, pois esta sim na variavel

nome = input ('Digite seu nome: ')
encontrar = input ('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
'''
Fatiamento de strings
 012345678
 Olá Mundo
-987654321
Fatiamento [i:f:p] [::]

O índice (i) é onde começa a exibição

(f) é até onde vai a contagem, o final. não é incluido na
exibição. Ex: print(variavel[0:2]), será exibido até "Ol" e
não sera mostrada a letra referente ao indice 2 (que é a letra "a")

O passo (p) é a sequencia de contagem. Ex. 2 - a contagem será 
realizada de 2 em dois... O passo negativo faz com que o codigo
seja lido de tras pra frente

Obs: a função len retorna a quantidade de caract. da str
é literalmente uma contagem de caracteres
'''
variavel = 'Olá mundo'
print(variavel[4:])

print(len(variavel[-9:]))
print(len(variavel))
print(variavel[0:9:2])
print(variavel[-1:-10:-2])
print(variavel[::-1])


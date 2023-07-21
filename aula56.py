'''
split e join com list e str
split - divite um string
strip - tira os espaços ('l' e 'r' para espaços a esquerda e direita)
join - une uma str
'''

frase = '      Olha só que   , coisa interessante     '
lista_frases = frase.split(', ')
print(lista_frases)

for i, frase in enumerate(lista_frases):
    print(lista_frases[i].strip())
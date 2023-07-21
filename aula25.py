'''
Interpolação básica de strings
s - string
d e i - int
f - float 
x e X - hexadecimal (ABCDEF0123456789)
%s %d %i %x... são chamados de placeholders

É UMA DAS OPÇÕES A SEREM ESCOLHIDAS ENTRE
F-STRING
.FORMAT
INTERPOLAÇÃO
'''
nome = 'Andrei'
preco = 1000.95897643
variavel = '%s, o preço total foi R$%.2f' % (nome, preco)
print (variavel)
print('O hexadecimal de %d é %08x' %(1500, 1500))
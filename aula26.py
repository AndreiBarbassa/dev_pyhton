'''
Formatação básica de strings
s - strings
d - int
f - float
.<número de dígitos>f
x ou X - hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Forç o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
'''
variavel = "ABC"
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{1000.0191209830482098:0=+10,.2f}')
print(f'O hexadecimal de 1500 é {1500:08x}')
print(f'{variavel!r}')





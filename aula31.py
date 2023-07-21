'''
Flag (bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = identidade
not -> signfica que está invertendo os valores

is -> condição
== -> condição tbm

É usado para saber se o interpretador entrou na condição ou não

'''
'''
condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True #nesse caso, condicao sendo false, a variável passou_no_if nunca foi criada, gerando erro no código abaixo
    print('Faça alguma coisa')
else:
    (print('Não faça algo'))

print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)
'''
condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True #nesse caso, condicao sendo false, a variável passou_no_if nunca foi criada, gerando erro no código abaixo
    print('Faça alguma coisa')
else:
    (print('Não faça algo'))




if passou_no_if is None:
    print('não passou no if')

if passou_no_if is not None:
    print('passou no if')






















#condição = false
'''
v1 = ('a')
v2 = ("q")

print(id(v1))
print(id(v2))
'''
#if condição:
#   print('Faça algo')
#else:
#   print('não faça algo')
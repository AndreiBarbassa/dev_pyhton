'''
Opecaração ternária (condicional de um linha)
<Valor> if <condição> else <outro valor>
'''
condicao = 10 == 10
variavel = 'valor' if condicao else 'outro valor'
print(variavel)

# digito = 9 # se digito > 9 = 0
# # novo_digito = digito if digito <= 9 else 0
# novo_digito = 0 if digito > 9 else digito
# print(novo_digito)

print('valor' if False else 'outro valor' if False else 'FIM')
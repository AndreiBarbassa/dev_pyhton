"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf_digitado = input('Digite apenas os números do CPF:' )

if cpf_digitado.isdigit():
    ind_0 = int(cpf_digitado [0]) * 10
    ind_1 = int(cpf_digitado [1]) * 9
    ind_2 = int(cpf_digitado [2]) * 8
    ind_3 = int(cpf_digitado [3]) * 7
    ind_4 = int(cpf_digitado [4]) * 6
    ind_5 = int(cpf_digitado [5]) * 5
    ind_6 = int(cpf_digitado [6]) * 4
    ind_7 = int(cpf_digitado [7]) * 3
    ind_8 = int(cpf_digitado [8]) * 2
    
    digitos_multiplicados = ind_0, ind_1, ind_2, ind_3, ind_4, ind_5, ind_6, ind_7, ind_8
    soma_da_multipllicação_dos_digitos = ind_0 + ind_1 + ind_2 + ind_3 + ind_4 + ind_5 + ind_6 + ind_7 + ind_8
    print(soma_da_multipllicação_dos_digitos)

    div_onze = soma_da_multipllicação_dos_digitos *10 % 11
    if div_onze > 9:
        print('o resultado aqui é zero pois o resto é maior que 9.')
    else:
        print(div_onze)
    ...
else:
    print('O valor digitado contém caracteres inválidos. Digite apenas números.')
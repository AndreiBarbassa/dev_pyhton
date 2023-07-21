'''
Faça uma lista de compras com listas.
O usuário deve ter a possibilidade de
Inserir, Apagar e Listas valores de sua lista
Não permita que o programa quebre com erros de índices
inexistentes na lista
'''
import os
lista = []

while True:
    print('Selecione uma opção: ')
    opcao = input("[i]nserir, [a]pagar, [l]istar: ")

    if opcao == 'i':
        valor = input('Digite o valor a ser adicionado: ')
        lista.append(valor)
        os.system('cls')

    elif opcao == 'a':
        indice_str = input('Digite o índice do valor a ser apagado: ')
        try:
            indice = int(indice_str)
            del lista[indice]
            os.system('cls')
        except Exception as e:
            os.system('cls')
            print('ERRO DESCONHECIDO.')


    elif opcao == 'l':
        for i, valor in enumerate(lista):
            print(i, valor)
            
        if len(lista) == 0:
            os.system('cls')
            print('Não há itens na lista')
    
    else:
        os.system('cls')
        print('Digite uma opção válida.')
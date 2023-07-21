"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

condicao = True

while condicao:
    nome = input ('Qual é o seu nome? ')
    print(f'seu nome é: {nome}')

    if nome == "sair":
        print('você saiu do loop')
        break
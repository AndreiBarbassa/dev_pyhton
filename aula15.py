#nome = input('Qual o seu nome?')
#print(f'O seu nome é {nome=}')

#numero_1 = input('Digite um número:') ex numero 1
#numero_2 = input('Digite outro número:') ex numero 5

#print(f'A soma dos números é: {numero_1 + numero_2}')
#ESSA CONCATENAÇÃO RETORNARA 15 POR SE TRATAR DE STR
#_________________________________________________________
#numero_1 = int(input('Digite um número: '))
#numero_2 = int(input('Digite outro número: '))

#print(f'A soma dos números é: {numero_1 + numero_2}')

#Transformar a variável em int dessa forma não permite
#verificação de erro
#___________________________________________________________

numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)


print(f'A soma dos números é: {numero_1 + numero_2}')

#dessa forma não há quebra no programa e é possível verificar 
#o que o usuário digitou, como por exemplo um número ou uma letra

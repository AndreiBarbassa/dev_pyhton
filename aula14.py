a = "AAAAA"
b = "BBBBB"
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format(nome1=a, nome2=b, nome3=c) 
#em python os argumentos se iniciam em 0, nesse caso é 0,1,2
#tudo que vem depois de um parâmetro deve ser nomeado tambem

print(formato)

print('"ja sei!"')


nome = "Luiz"
idade = 23
forma = '{1} tem {0} anos'
print(forma.format(nome,idade))



# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
#  tipos imutáveis e primitivos:
# str, int, float, bool
print(int('1'), type(int('1')))
print(type(float('1') + 1))
print(bool(' ')) # Bool contendo espaço é verdadeiro
print(bool('')) # Bool vazio é falso
print(str(11) + 'b') # Int convertido em str
# não é possível transformar letras em int
print('a' + 'b')
print(1+1) # Nesse caso foi usado dois int
print('1'+'1') # Nesse caso eu usei duas strings
print(int('1') + 1.0) # Conversão de str em int somado com float

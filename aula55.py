"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""
import decimal

numero1 = decimal.Decimal(str(0.1))
numero2 = decimal.Decimal(str(0.7))
numero3 = numero1 + numero2
print(f'{numero3:.2f}')
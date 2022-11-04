# Cara coroa
import math
import random

# random.randint(a, b) : retorna um número
# inteiro pseudo randômico  n, a <= n <= b
numero = random.randint(0, 1)

chute = input('Informe 0. cara ou 1. coroa: ')
chute = int(chute)

if (numero == chute):
    print('Você acertou. Deu: {}'.format(numero))
else:
    print('Você errou. Deu: {}'.format(numero))

# IMC : Índice de massa corporea
"""
Fonte https://www.saude.rj.gov.br/obesidade/calcule-seu-imc
RESULTADO	SITUAÇÃO
Abaixo de 17	Muito abaixo do peso
Entre 17 e 18,49	Abaixo do peso
Entre 18,5 e 24,99	Peso normal
Entre 25 e 29,99	Acima do peso
Entre 30 e 34,99	Obesidade I
Entre 35 e 39,99	Obesidade II (severa)
Acima de 40	Obesidade III (mórbida)
"""
massa = float(input('Informe seu peso em kg: '))
altura = float(input('Informe sua altura em m: '))
imc = massa / pow(altura, 2)
if (imc < 17):
    print('Muito abaixo do peso. IMC = {}'.format(imc))
elif (imc >= 17 and imc < 18.5):
    print('Abaixo do peso. IMC = {}'.format(imc))
elif (imc >= 18.5 and imc < 25):
    print('Peso normal. IMC = {}'.format(imc))
elif (imc >= 25 and imc < 30):
    print('Acima do peso. IMC = {}'.format(imc))
elif (imc >= 30 and imc < 35):
    print('Obesidade I. IMC = {}'.format(imc))
elif (imc >= 35 and imc < 40):
    print('Obesidade II (severa). IMC = {}'.format(imc))
else:
    print('AObesidade III (mórbida). IMC = {}'.format(imc))

#
'''Fórmula de Bhaskara
Fonte 1: https://en.wikipedia.org/wiki/Bh%C4%81skara_II
https://pt.khanacademy.org/
testes: 
2,4,2
1,4,-21
3,6,10
'''
print('Informe os coeficientes a, b, c ')
print('de uma equação no formato ax² + bx + c = 0')
a =  float(input())
b =  float(input())
c =  float(input())

delta = pow(b,2) - (4 * a * c)

if(delta == 0):
    x1= -b/(2 *a)
    print('Equação tem uma raiz real. '
          'x1 = {}'.format(x1))
elif( delta > 0):
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)
    print('Equação tem duas raízes reais'
          'x1 = {} e x2 = {}'.format(x1, x2))
else:
    print('Equação não tem raízes reais')

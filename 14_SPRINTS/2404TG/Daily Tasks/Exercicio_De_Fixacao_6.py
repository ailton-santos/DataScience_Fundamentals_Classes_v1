# -*- coding: utf-8 -*-
"""menorEMaiorNumero0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TLmScmCoRHuwncpVS07VOH4uXuW9CVrf
"""

qntd = 1
maior = -1
menor = 10000000000000000000000000000
numeros = 0

while qntd <= 10:
  numero = int(input(f'Digite o {qntd}º numero: '))

  if numero > maior:
    maior = numero

  if numero < menor:
    menor = numero

  numeros = numeros + numero
  qntd = qntd + 1

print(f'Menor numero: {menor}')
print(f'Maior numero: {maior}')
print('Media da soma: ', numeros/qntd)
# -*- coding: utf-8 -*-
"""Untitled36.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vQQjQOI5Y9M0G37SctKdB1BU6CMcjUQS
"""

def verifica_sinal(numero):

  if numero >0:
    return 'P' # Positivo
  elif numero == 0:
    return 'N' # Zero
  else:
    return 'N' # Negativo

#Exemplo de uso
valor= float(input("Digite um numero: "))
resultado= verifica_sinal(valor)
print(f"O sinal do numero é: {resultado}")
# -*- coding: utf-8 -*-
"""Compras_com_juros.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11_pwF-J-KM1GSsrDaHa8iNqzRGIqho1b
"""

valor_de_compra = float(input('Infome o valor da compra '))
numero_de_prestacoes = int(input('Informe o números de parcelas '))

valor_das_parcelas = (valor_de_compra / numero_de_prestacoes)

print(valor_das_parcelas)

juros = valor_das_parcelas*(0.02)

#valor_total_com_juros = valor_das_parcelas + juros
print("Valor total com juros:", (valor_das_parcelas+juros))

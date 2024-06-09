# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1uWzh9Efopamz1SCUqPS3uyWNBormxMlV
"""

idades = []
sexos = []

for i in range(1, 11):
    idade = int(input(f'Me informe a idade da {i}ª pessoa: '))
    sex = input(f'Selecione o sexo da {i}ª pessoa (M / F): ').upper()

    while sex not in ['M', 'F']:
        print("Por favor, digite 'M' para masculino ou 'F' para feminino.")
        sex = input(f'Selecione o sexo da {i}ª pessoa (M / F): ').upper()

    idades.append(idade)
    sexos.append(sex)

idades_mulheres = [idades[i] for i in range(len(sexos)) if sexos[i] == 'F']
idades_homens = [idades[i] for i in range(len(sexos)) if sexos[i] == 'M']
idades_grupo = idades

media_mulheres = sum(idades_mulheres) / len(idades_mulheres) if idades_mulheres else 0
media_homens = sum(idades_homens) / len(idades_homens) if idades_homens else 0
media_grupo = sum(idades_grupo) / len(idades_grupo) if idades_grupo else 0

print(f'Média das idades das mulheres: {media_mulheres:.2f}')
print(f'Média das idades dos homens: {media_homens:.2f}')
print(f'Média das idades do grupo: {media_grupo:.2f}')
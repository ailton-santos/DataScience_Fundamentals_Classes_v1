# -*- coding: utf-8 -*-
"""Untitled15.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GFFugKR4xlrEr27Tt0l4wuKMm9l6MI00
"""

import pandas as pd
import numpy as np

s1=pd.Series([1,2,-5,0])

s1

s1.index

s1.values

#Nomeando os Rotulos.
s2 = pd.Series([ 1,  2, -5,  0],index=['a', 'b','c', 'd'])
s2

#Mostrar o index
s2.index

#Inputar ou adiconar dados de acordo com uma Label
s2['joao'] = 1000
s2

#Comparação (qual numero é maior que 0 dentro do dataset)
s2[s2>0]

#Algebra
s2*2

#Verificar se nula(vazio)
s2.isnull()

#Como criar um Data Frame
dados={'estado':['SP','MG','PR','SP','MG','PR'],
       'ANO':[2019,2019,2019,2020,2020,2020],
       'POP':[45.9,21.2,16.7,46.7,21.4,17.3]}
dados1 = pd.DataFrame(dados)
dados1

#Mostrar so as primeiras 5 linhas
dados1.head(2)
#Mostrar as ultimas 5 linhas
dados1.tail(2)

#Amostra do DataFrame de formas aleatorias
dados1.sample(2)

#Novo Data Frame a partir do anterior (Para teste por exemplo)
df2=pd.DataFrame(dados1,columns=['ANO','estado','POP'])
df2

#Mostrar variavel ou label
dados1 = ['estado'] #nome da coluna dos dados (Label)

#Como mostrar a vizualização de duas variaveis ao mesmo  tempo/ atv casa
colunas_selecionadas = df2.iloc[:, [0, 1]]
colunas_selecionadas

#Verificar os tipos de dados
df2.dtypes

#Atribuir valores ao Data Frame
df2['estimativa']=50
df2

#Fazer a contagem por linhas para viualzar dados
df2['estimativa']=np.arange(6)
df2

#Segmentar dados
df3=df2

df3=df2['ANO']
df3

#Deu ruim deleta, Atividade casa
del df2['ANO']

#Entender o Data Frame, quantas linhas e quantas colunas
df2.shape

colunas_selecionadas = df2.iloc[:, [0, 1]]
colunas_selecionadas
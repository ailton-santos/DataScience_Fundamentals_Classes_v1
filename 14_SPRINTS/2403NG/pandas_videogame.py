# -*- coding: utf-8 -*-
"""Pandas_videogame.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UdWO4ONkuaq6wUVNWUX58qCZacNzuyUa
"""

import pandas as pd

file_name='video_games1.csv'
df=pd.read_csv('video_games1.csv')
print(df.head())

df['Title']=df['Title'].str.lower()

entrada=input('Digite o nome do jogo ou parte do nome:').lower()

Results=df[df['Title'].str.contains(entrada)]

for index,jogo in Results.iterrows():
  print(jogo['Title'].title())
  print("Plataforma:",jogo['Metadata.Publishers'])
  print("Ano:",jogo['Release.Year'])
  print("Gênero:",jogo['Metadata.Genres'])
  print()

colunas_desejadas=['Title','Metadata.Publishers','Release.Year','Metadata.Genres','Release.Console']
for index,jogo in Results.iterrows():
  print(jogo.loc[colunas_desejadas].to_frame().T.to_string(index=False))
  print("\n")
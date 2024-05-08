# -*- coding: utf-8 -*-
"""regressao_linear_p1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18M9PDDPhCO5P5jZtKlFDrIiGslckXdmT
"""

import statistics as st

x=[1,2,3,4,5]
y=[2,3,4,5,6]

media_x=st.mean(x)
media_y=st.mean(y)

covariance= sum((x[i] - media_x)*(y[i] - media_y) for i in range(len(x)))

variance=sum((x[i]- media_x)** 2 for i in range (len(x)))

#coeficiente de inclinação
b1=covariance/variance

#coeficiente de intercepto
b0= media_y-b1*media_x

print('O coeficiente de inclinação é: ',b1)
print('O coeficiente de intercepto é:',b0)
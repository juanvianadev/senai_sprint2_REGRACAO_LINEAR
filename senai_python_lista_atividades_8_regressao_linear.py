# -*- coding: utf-8 -*-
"""SENAI-Python-Lista-Atividades-8-REGRESSAO_LINEAR.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Tg2r10IQgvTdVc_uhfAFmHK1Ljn1lrvq
"""

import numpy as np
import matplotlib.pyplot as plt

df = np.load('combustivel_e_temperatura.npy')

df

x, y = df

plt.scatter(x, y)
plt.xlabel('combustivel')
plt.ylabel('temperatura')
plt.title('Grafico')
plt.grid()
plt.show()

# solução np.lstsq
X = np.vstack((np.ones(len(x)), x)).T
betas, res, _, _ = np.linalg.lstsq(X, y, rcond=None)
beta0, beta1 = betas
residuo = res[0]

# Calculando a previsão do modelo
yPrev = beta1 * x + beta0

# Calculando R-Quadrado
yMedio = np.mean(y)
tss = np.sum((y - yMedio) ** 2) # Soma total dos quadrados
rss = np.sum((y - yPrev) ** 2) # residuo dos quadrados
r2 = 1 - rss / tss

#Printando cada variavel
print(f'\nIntercepto, {beta0 = :.5f}')
print(f'Coeficiente angular, {beta1 = :.5f}')
print(f'R-quadrado, {r2 = :.5f}')
print(f'Residuo de lstsq, {residuo = :.5f}')
print(f'Residuo calculado, {rss = :.5f}\n')

#comparação com pontos preditos pelo modelo
plt.scatter(x, y, label='Dados')
#plt.scatter(x, yPrev, label='Modelo')
plt.plot(x, beta0 + beta1 * x, 'r--', alpha = 0.2)
plt.xlabel('Litros por minuto')
plt.ylabel('Temperatura do motor')
plt.legend()
plt.grid()

#caso seja 8 litros
resultado = beta1 * 8 + beta0
print(np.round(resultado,1))
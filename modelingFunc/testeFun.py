from functions1 import *
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

Y = []
X = np.arange(2,12)

for x in X:
    value = 2 + 5 * x
    # value = 15 + 22 * x + 30 * (x**2) + 123 * (x**6) # POLI
    # value = np.log(x) # * ( 1 + np.random.random() * 0.15 * (-1 ** x)) # LN ou EXP

    Y.append( value)

janela = 5

medMovExp = media_movel_exponencial(Y,janela)
medMovArt = media_movel_aritmetica(Y,janela)

RegExp = exponential_regression(X,Y)
RegLN = logarithmic_regression(X,Y)
RegPoli = polynomial_regression(X,Y,6)


plt.plot(X,Y, label="Input")

# Plot de Medias Móveis

# plt.plot(X,medMovExp, label="Exponencial")
# plt.plot(X[janela - 1:len(X)],medMovArt, label="Aritm")

#Plot de Regressões

# plt.plot(X, RegExp,label="Reg Exp")
# plt.plot(X, RegLN,label="Reg LN")

plt.plot(X, RegPoli,label="Reg Polinomial")


# plt.ylim(5,15)
# plt.xlim(115,120)
plt.legend()
plt.show()

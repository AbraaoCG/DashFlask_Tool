import numpy as np

def media_movel_aritmetica(dados, janela):
    """
    Calcula a média móvel aritmética dos dados com a janela especificada.
    
    Parâmetros:
    dados (list): Lista de valores numéricos.
    janela (int): Número de pontos a serem considerados para o cálculo da média móvel.
    
    Retorna:
    list: Lista de valores da média móvel aritmética.
    """
    media = []
    for i in range(len(dados) - janela + 1):
        media.append(sum(dados[i:i+janela]) / janela)
    return media

def media_movel_exponencial(dados, janela):
    """
    Calcula a média móvel exponencial dos dados com a janela especificada.
    
    Parâmetros:
    dados (list): Lista de valores numéricos.
    janela (int): Número de pontos a serem considerados para o cálculo da média móvel.
    
    Retorna:
    list: Lista de valores da média móvel exponencial.
    """
    media = []
    alpha = 2 / (janela + 1)
    media.append(dados[0])
    for i in range(1, len(dados)):
        valor_atual = dados[i]
        valor_anterior = media[-1]
        media_atual = alpha * valor_atual + (1 - alpha) * valor_anterior
        media.append(media_atual)
    return media


def media_movel(dados, janela, tipo=0):
    """
    Calcula a média móvel dos dados com a janela especificada e o tipo especificado.
    
    Parâmetros:
    dados (list): Lista de valores numéricos.
    janela (int): Número de pontos a serem considerados para o cálculo da média móvel.
    tipo (int): Tipo de média móvel a ser calculada: 0 para aritmética (padrão) ou 1 para exponencial.
    
    Retorna:
    list: Lista de valores da média móvel.
    """
    if tipo == 0:
        return media_movel_aritmetica(dados, janela)
    elif tipo == 1:
        return media_movel_exponencial(dados, janela)
    else:
        raise ValueError("Tipo de média móvel inválido. Use 0 para aritmética ou 1 para exponencial.")
    

def linear_regression_aux(x, y):
    n = len(x)
    sumx = np.sum(x)
    sumy = np.sum(y)
    sumxy = np.sum(x * y)
    sumx2 = np.sum(x ** 2)
    det = n * sumx2 - sumx ** 2

    if abs(det) <= 0.000001:
        print("ERROR: Determinant is null!!!")
        print("ERROR: Stop program")
        return None, None

    a0 = (-sumx * sumxy + sumy * sumx2) / det
    a1 = (n * sumxy - sumx * sumy) / det

    return a0, a1


def logarithmic_regression(X, Y):
    x_ln = np.log(X)
    # a1, a0 = np.polyfit(x_ln, Y, 1)
    a0,a1 = linear_regression_aux(x_ln,Y)
    y_pred = a0 + a1 * x_ln
    return y_pred

def exponential_regression(X, y):
    y_ln = np.log(y)
    a1, a0 = np.polyfit(X, y_ln, 1)
    a0_exp = np.exp(a0)

    y_pred = a0_exp * np.exp(a1 * X) 
    return y_pred

def polynomial_regression(X, Y, degree):
    z = np.polyfit(X, Y, degree)
    p = np.polyval(z,X)
    return p

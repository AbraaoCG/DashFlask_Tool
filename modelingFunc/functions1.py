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

def linearSolver(A,X,B):
    # Resolver A . X = B 
    pass

# def invert_matrix(A):
#     n = len(A)
#     A_inv = [[0.0] * n for i in range(n)]
    
#     # Criar matriz identidade
#     for i in range(n):
#         A_inv[i][i] = 1.0
    
#     # Eliminação Gaussiana com pivoteamento parcial
#     for j in range(n):
#         # Escolher o pivô
#         max_row = j
#         for i in range(j+1, n):
#             if abs(A[i][j]) > abs(A[max_row][j]):
#                 max_row = i
#         # Trocar linhas para obter o pivô na diagonal principal
#         A[j], A[max_row] = A[max_row], A[j]
#         A_inv[j], A_inv[max_row] = A_inv[max_row], A_inv[j]
        
#         # Reduzir a matriz abaixo da diagonal principal
#         for i in range(j+1, n):
#             factor = A[i][j] / A[j][j]
#             for k in range(j, n):
#                 A[i][k] -= factor * A[j][k]
#                 A_inv[i][k] -= factor * A_inv[j][k]
    
#     # Resolver a matriz triangular superior
#     for j in range(n-1, -1, -1):
#         for i in range(j-1, -1, -1):
#             factor = A[i][j] / A[j][j]
#             for k in range(n):
#                 A_inv[i][k] -= factor * A_inv[j][k]
#             A[i][j] = 0
    
#     # Dividir cada linha pelo elemento diagonal
#     for i in range(n):
#         diag = A[i][i]
#         for j in range(n):
#             A_inv[i][j] /= diag
    
#     return A_inv

# def polyfit(x, y, degree):
#     # Número de pontos
#     n = len(x)
#     # Inicializa as matrizes
#     X = np.zeros((n, degree+1))
#     Y = np.zeros((n, 1))
    
#     # Preenche a matriz X com as potências de x até o grau desejado
#     for i in range(n):
#         for j in range(degree+1):
#             X[i][j] = x[i]**j
    
#     # Preenche a matriz Y com os valores de y
#     for i in range(n):
#         Y[i][0] = y[i]
    
#     # Calcula a matriz A, que é a solução do sistema de equações normais
#     linearSolver()
    
#     # Calcula os valores de y preditos pela regressão polinomial
#     y_pred = np.zeros(n)
#     for i in range(n):
#         for j in range(degree+1):
#             y_pred[i] += A[j][0] * (x[i]**j)
    
#     # Retorna os coeficientes da regressão e os valores de y preditos
#     return A, y_pred

def polynomial_regression(x, y, degree):
    z = np.polyfit(x, y, degree)
    p = np.polyval(z,X)
    return p
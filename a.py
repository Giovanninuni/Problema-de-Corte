import numpy as np
import math

# Dados de Entrada
L = 194 # Comprimento do objeto em estoque
itens = [
    {"comprimento": 108, "demanda": 4}, #item 0
    {"comprimento": 13, "demanda": 8}, #item 1
    {"comprimento": 90, "demanda": 7} #item 2
]
m = len(itens) # Retorna o numero de itens que "itens" contem

# Inicializar a Matriz Básica (m x m) e o Vetor de Custo cB (m x 1)

# Cria uma matriz m x m cheia de zeros
B = np.zeros((m, m)) 

# Cria um vetor de custo m x 1 cheio de '1's
# O custo de cada padrão homogêneo é 1
cB = np.ones(m) 

# Preenche a diagonal da matriz B
for i in range (m): 
    l_i = itens[i]["comprimento"]
    d_i = itens[i]["demanda"]

    # Calculo de quantos itens i cabem em L
    # Equacao (6) do PDF

    num_itens_no_padrao = math.floor(L / l_i) # math.florr arredonda para o inteiro abaixo
    # ex: itens[0] -> num_itens_no_padrao = 1
    # itens[1] -> num_itens_no_padrao = 14

    valor_diagonal = min(num_itens_no_padrao, d_i)
    

import numpy as np
import math

# O que esse arquivo faz:
# O passo de "Inicialização"  dos algoritmos 1 e 3. 
# Preparando todas as variáveis necessárias para iniciar a primeira iteração do método Simplex.

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
    l_i = itens[i]["comprimento"] # Comprimento do item i
    d_i = itens[i]["demanda"] # Demanda, numero total que precisamos produzir de i

    # Calculo de quantos itens i cabem em L
    # Equacao (6) do PDF

    num_itens_no_padrao = math.floor(L / l_i) # math.florr arredonda para o inteiro abaixo
    # ex: itens[0] -> num_itens_no_padrao = 1
    # itens[1] -> num_itens_no_padrao = 14

    # Para inserir na matriz, vemos qual valor é menor entre o numero de itens e a demanda
    # evitando assim produzir mais do que a demanda
    # Ou seja, produz no máximo a demanda total
    valor_diagonal = min(num_itens_no_padrao, d_i) # min() retorna o minimo valor entre os dois
    # ex: itens[1] -> min(14, 8) = 8

    # Inserimos o valor
    B[i][i] = valor_diagonal 
# Fim do loop for

print("--- Matriz Basica Inicial B---")
print(B)

print("--- Vetor de Custo ---")
print(cB)

# Vetor de Demanda d (d na equação Ax = d)
d = np.array([item["demanda"] for item in itens])
print("--- Vetor de Demanda ---")
print(d)

# Edicao para teste

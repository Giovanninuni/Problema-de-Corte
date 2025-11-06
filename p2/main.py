import numpy as np
import math

# Importa o nosso outro arquivo, "mochila.py"
import mochila

print("--- [MAIN] Executando main.py ---")

# --- Passo 1: Inicialização (O que já fizemos) ---
# [cite: 170-174]
L = 194 # Comprimento do objeto em estoque
itens = [
    {"comprimento": 108, "demanda": 4}, # item 0
    {"comprimento": 13,  "demanda": 8}, # item 1
    {"comprimento": 90,  "demanda": 7}  # item 2
]
m = len(itens)

# Vetor de Demanda d
d = np.array([item["demanda"] for item in itens])

# Matriz Básica Inicial B e Vetor de Custo cB
B = np.zeros((m, m))
cB = np.ones(m)

for i in range(m):
    l_i = itens[i]["comprimento"]
    d_i = itens[i]["demanda"]
    
    # Equação (6) [cite: 150]
    num_itens_no_padrao = math.floor(L / l_i)
    valor_diagonal = min(num_itens_no_padrao, d_i)
    
    B[i, i] = valor_diagonal

print("\n[MAIN] Matriz Básica Inicial B:")
print(B)
print("\n[MAIN] Vetor de Custo cB:")
print(cB)

# --- Passo 2: Calcular Lambda (Início do loop Simplex) ---
# [cite: 178-179]
#
# O Algoritmo 1 diz para determinar a solução dual (lambda)
# resolvendo B^T * lambda = cB.
#
# Nota: Como B é diagonal, B.T (Transposta de B) é igual a B.
# Vamos usar B.T por correção, embora B funcione igual neste caso.
try:
    # Solucionador de sistema linear do NumPy: A * x = b  ->  x = np.linalg.solve(A, b)
    # A = B.T , x = lambda_ , b = cB
    lambda_ = np.linalg.solve(B.T, cB) 
    
    print(f"\n[MAIN] Solução Dual (lambda) calculada:")
    print(lambda_)

    # --- Passo 3: Chamar o Problema da Mochila ---
    # 
    #
    # Agora, passamos L, os itens, e o lambda_ calculado
    # para a nossa função em mochila.py
    
    print("\n[MAIN] >>> Chamando mochila.resolver_mochila...")
    
    novo_padrao, valor_padrao = mochila.resolver_mochila(L, itens, lambda_)

    print("\n[MAIN] <<< Retornou para main.py")
    print(f"[MAIN] Novo padrão retornado (atualmente dummy): {novo_padrao}")
    print(f"[MAIN] Valor do padrão retornado: {valor_padrao}")

except np.linalg.LinAlgError:
    print("\n[MAIN] Erro: A matriz B é singular, não foi possível calcular lambda.")


print("\n--- [MAIN] Fim da execução main.py ---")
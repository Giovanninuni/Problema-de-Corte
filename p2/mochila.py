import numpy as np

# O problema da Mochila:
# Em cada iteração, ele será chamado para encontrar o melhor novo padrão de corte para adicionar à nossa solução.


def resolver_mochila(L, itens, lambda_):
    """
    Resolve o Problema da Mochila usando o Algoritmo 2 (Enumeração Implícita).

    Argumentos:
    L (float): A capacidade da mochila (comprimento do objeto).
    itens (list): A lista de itens (com 'comprimento' e 'demanda').
    lambda_ (np.array): O vetor de 'utilidade' (variáveis duais, v_i).

    Retorna:
    np.array: O melhor padrão (coluna 'a') encontrado.
    float: O valor g(a) desse padrão.
    """

    print(f"\n--- Resolvendo Problema da Mochila ---")
    print(f"Capacidade L: {L}")
    print(f"Valores de Utilidade (lambda): {lambda_}")

    m = len(itens) # Retorna o numero de itens do parametro "itens"

    # Parte 1: Inicialização e Ordenação (Algoritmo 2)

    itens_mochila = []
    for i in range(m):
        comprimento = itens[i]["comprimento"]
        demanda = itens[i]["demanda"]
        utilidade = lambda_[i]

        # Corrige caso improvável de comprimento = 0
        if comprimento > 0:
            eficiencia = utilidade / comprimento
        else:
            eficiencia = 0

        # Insere no final da lista
        itens_mochila.append(
        { 
            "id_original": i,
            "comprimento": comprimento,
            "demanda": demanda,         
            "utilidade": utilidade,     
            "eficiencia": eficiencia
        })
    # Fim do loop for
    
    # Funcao sorted: (interable, key, reverse)
    # Ordena o interável "itens_mochila", com base na chave eficiencia, em ordem decrescente
    itens_ordenados = sorted(itens_mochila, key = lambda x: x["eficiencia"], reverse=True)

    print("\nItens ordenados por eficiencia (lambda/comprimento):")
    for item in itens_ordenados:
        print(f"  ID: {item['id_original']}, l_i: {item['comprimento']}, v_i: {item['utilidade']:.3f}, Eficiencia: {item['eficiencia']:.4f}")

    # Próximos passos: Implementar a busca
    # Por enquanto, vamos retornar um padrão vazio

    melhor_padrao = np.zeros(m, dtype=int)
    melhor_valor = 0

    print("-------------------------------------")

    return melhor_padrao, melhor_valor
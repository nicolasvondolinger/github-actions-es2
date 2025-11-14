"""
Este módulo implementa a lógica para contar componentes conectados em um grafo
usando Busca em Profundidade (DFS).
"""

def dfs(v, visited, graph):
    """
    Função auxiliar recursiva para a Busca em Profundidade (DFS).
    """
    visited.add(v)
    # O grafo é representado como um dicionário de adjacências (lista ou set)
    # graph.get(v, []) lida com nós que não têm arestas de saída
    for neighbor in graph.get(v, []):
        if neighbor not in visited:
            dfs(neighbor, visited, graph)

def count_components(n, graph):
    """
    Conta o número de componentes conectados em um grafo não direcionado.

    Args:
        n (int): O número de vértices (os vértices são indexados de 0 a n-1).
        graph (dict): Um dicionário representando a lista de adjacência do grafo.
                      Ex: {0: [1], 1: [0, 2], 2: [1], 3: [4], 4: [3]}
    
    Returns:
        int: O número de componentes conectados.
    """
    if n == 0:
        return 0

    visited = set()
    component_count = 0

    # Itera por todos os vértices de 0 a n-1
    for i in range(n):
        if i not in visited:
            dfs(i, visited, graph)
            component_count += 1
    
    return component_count
def dfs(v, visited, graph):
    visited.add(v)
    for neighbor in graph.get(v, []):
        if neighbor not in visited:
            dfs(neighbor, visited, graph)

def count_components(n, graph):
    if n == 0:
        return 0

    visited = set()
    component_count = 0

    for i in range(n):
        if i not in visited:
            dfs(i, visited, graph)
            component_count += 1
    
    return component_count
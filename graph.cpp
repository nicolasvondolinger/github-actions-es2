#include "graph.h"

// Implementação da DFS
void dfs(int v, std::vector<bool>& visited, const std::vector<std::vector<int>>& graph) {
    visited[v] = true;
    for (auto const& w : graph[v]) {
        if (!visited[w]) {
            dfs(w, visited, graph);
        }
    }
}

// Implementação da contagem de componentes
int countComponents(int n, const std::vector<std::vector<int>>& graph) {
    if (n == 0) return 0;

    std::vector<bool> visited(n, false);
    int componentCount = 0;

    for (int i = 0; i < n; ++i) {
        if (!visited[i]) {
            dfs(i, visited, graph);
            componentCount++;
        }
    }

    return componentCount;
}
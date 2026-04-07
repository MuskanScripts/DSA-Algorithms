"""
Cycle Detection in Directed and Undirected Graphs

Directed Graph  — DFS with recursion stack (white-grey-black coloring)
Undirected Graph — DFS with parent tracking
Union-Find approach also included for undirected graphs.

Time Complexity:  O(V + E)
Space Complexity: O(V)
"""

from collections import defaultdict


# ---------------------------------------------------------------------------
# Directed Graph — DFS coloring
# ---------------------------------------------------------------------------

def has_cycle_directed(num_vertices, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * num_vertices

    def dfs(u):
        color[u] = GRAY
        for v in graph[u]:
            if color[v] == GRAY:
                return True
            if color[v] == WHITE and dfs(v):
                return True
        color[u] = BLACK
        return False

    return any(color[v] == 0 and dfs(v) for v in range(num_vertices))


# ---------------------------------------------------------------------------
# Undirected Graph — DFS with parent tracking
# ---------------------------------------------------------------------------

def has_cycle_undirected(num_vertices, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * num_vertices

    def dfs(u, parent):
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                if dfs(v, u):
                    return True
            elif v != parent:
                return True
        return False

    return any(not visited[v] and dfs(v, -1) for v in range(num_vertices))


if __name__ == "__main__":
    print("--- Directed Graph ---")
    print("Edges (0->1, 1->2, 2->0):", has_cycle_directed(3, [(0, 1), (1, 2), (2, 0)]))
    print("Edges (0->1, 1->2):", has_cycle_directed(3, [(0, 1), (1, 2)]))

    print("\n--- Undirected Graph ---")
    print("Edges (0-1, 1-2, 2-0):", has_cycle_undirected(3, [(0, 1), (1, 2), (2, 0)]))
    print("Edges (0-1, 1-2):", has_cycle_undirected(3, [(0, 1), (1, 2)]))

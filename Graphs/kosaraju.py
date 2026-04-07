"""
Strongly Connected Components — Kosaraju's Algorithm

Finds all SCCs in a directed graph using two DFS passes.

Time Complexity:  O(V + E)
Space Complexity: O(V)
"""

from collections import defaultdict


class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def _dfs_finish_order(self, v, visited, stack):
        visited.add(v)
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self._dfs_finish_order(neighbor, visited, stack)
        stack.append(v)

    def _transpose(self):
        transposed = Graph(self.n)
        for u in self.graph:
            for v in self.graph[u]:
                transposed.add_edge(v, u)
        return transposed

    def _dfs_collect(self, v, visited, component):
        visited.add(v)
        component.append(v)
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self._dfs_collect(neighbor, visited, component)

    def kosaraju_scc(self):
        # Pass 1: fill finish-order stack
        visited = set()
        stack = []
        for v in range(self.n):
            if v not in visited:
                self._dfs_finish_order(v, visited, stack)

        # Pass 2: traverse transposed graph in reverse finish order
        transposed = self._transpose()
        visited = set()
        sccs = []
        while stack:
            v = stack.pop()
            if v not in visited:
                component = []
                transposed._dfs_collect(v, visited, component)
                sccs.append(component)

        return sccs


if __name__ == "__main__":
    g = Graph(5)
    edges = [(1, 0), (0, 2), (2, 1), (0, 3), (3, 4)]
    for u, v in edges:
        g.add_edge(u, v)

    sccs = g.kosaraju_scc()
    print("Strongly Connected Components (Kosaraju):")
    for i, scc in enumerate(sccs):
        print(f"  SCC {i + 1}: {scc}")

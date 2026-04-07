"""
Strongly Connected Components — Tarjan's Algorithm

Finds all SCCs in a directed graph in a single DFS pass using
a stack and low-link values.

Time Complexity:  O(V + E)
Space Complexity: O(V)
"""

from collections import defaultdict


class TarjanSCC:
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def find_sccs(self):
        disc = [-1] * self.n
        low = [0] * self.n
        on_stack = [False] * self.n
        stack = []
        timer = [0]
        sccs = []

        def dfs(u):
            disc[u] = low[u] = timer[0]
            timer[0] += 1
            stack.append(u)
            on_stack[u] = True

            for v in self.graph[u]:
                if disc[v] == -1:
                    dfs(v)
                    low[u] = min(low[u], low[v])
                elif on_stack[v]:
                    low[u] = min(low[u], disc[v])

            # u is a root of an SCC
            if low[u] == disc[u]:
                component = []
                while True:
                    w = stack.pop()
                    on_stack[w] = False
                    component.append(w)
                    if w == u:
                        break
                sccs.append(component)

        for v in range(self.n):
            if disc[v] == -1:
                dfs(v)

        return sccs


if __name__ == "__main__":
    t = TarjanSCC(5)
    edges = [(1, 0), (0, 2), (2, 1), (0, 3), (3, 4)]
    for u, v in edges:
        t.add_edge(u, v)

    sccs = t.find_sccs()
    print("Strongly Connected Components (Tarjan):")
    for i, scc in enumerate(sccs):
        print(f"  SCC {i + 1}: {scc}")

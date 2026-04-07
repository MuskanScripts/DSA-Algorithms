"""
Depth First Search (DFS) — Graph Algorithm

Traverses a graph by exploring as far as possible along each branch
before backtracking.

Supports both directed and undirected graphs represented as adjacency lists.

Time Complexity:  O(V + E)
Space Complexity: O(V)
"""

from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_recursive(self, start):
        """DFS using recursion."""
        visited = set()
        result = []

        def dfs(node):
            visited.add(node)
            result.append(node)
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(start)
        return result

    def dfs_iterative(self, start):
        """DFS using an explicit stack."""
        visited = set()
        stack = [start]
        result = []

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                result.append(node)
                for neighbor in reversed(self.graph[node]):
                    if neighbor not in visited:
                        stack.append(neighbor)

        return result


if __name__ == "__main__":
    g = Graph()
    edges = [(0, 1), (0, 2), (1, 2), (2, 0), (2, 3), (3, 3)]
    for u, v in edges:
        g.add_edge(u, v)

    print("DFS (recursive) from node 2:", g.dfs_recursive(2))
    print("DFS (iterative) from node 2:", g.dfs_iterative(2))

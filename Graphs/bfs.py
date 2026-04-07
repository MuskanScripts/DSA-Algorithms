"""
Breadth First Search (BFS) — Graph Algorithm

Traverses a graph level by level using a queue.

Supports both directed and undirected graphs represented as adjacency lists.

Time Complexity:  O(V + E)
Space Complexity: O(V)
"""

from collections import defaultdict, deque


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start):
        visited = {start}
        queue = deque([start])
        result = []

        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return result

    def shortest_path(self, start, end):
        """Returns the shortest path from start to end (unweighted graph)."""
        if start == end:
            return [start]

        visited = {start}
        queue = deque([(start, [start])])

        while queue:
            node, path = queue.popleft()
            for neighbor in self.graph[node]:
                if neighbor == end:
                    return path + [neighbor]
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))

        return []  # No path found


if __name__ == "__main__":
    g = Graph()
    edges = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 4), (3, 4)]
    for u, v in edges:
        g.add_edge(u, v)

    print("BFS from node 0:", g.bfs(0))
    print("Shortest path 0 -> 4:", g.shortest_path(0, 4))

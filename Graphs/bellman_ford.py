"""
Bellman-Ford Algorithm — Shortest Path with Negative Weights

Finds shortest paths from a source vertex to all other vertices.
Unlike Dijkstra, it handles graphs with negative edge weights and
can detect negative weight cycles.

Time Complexity:  O(V * E)
Space Complexity: O(V)
"""


def bellman_ford(num_vertices, edges, source):
    """
    edges: list of (u, v, weight)
    Returns: (dist, has_negative_cycle)
    """
    dist = [float('inf')] * num_vertices
    dist[source] = 0

    # Relax all edges V-1 times
    for _ in range(num_vertices - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Check for negative weight cycles
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            return dist, True  # Negative cycle detected

    return dist, False


if __name__ == "__main__":
    # Example graph with 5 vertices
    edges = [
        (0, 1, -1),
        (0, 2, 4),
        (1, 2, 3),
        (1, 3, 2),
        (1, 4, 2),
        (3, 2, 5),
        (3, 1, 1),
        (4, 3, -3),
    ]
    source = 0
    dist, neg_cycle = bellman_ford(5, edges, source)

    if neg_cycle:
        print("Graph contains a negative weight cycle!")
    else:
        print(f"Shortest distances from node {source}:")
        for i, d in enumerate(dist):
            print(f"  Node {i}: {d}")

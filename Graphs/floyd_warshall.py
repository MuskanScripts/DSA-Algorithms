"""
Floyd-Warshall Algorithm — All-Pairs Shortest Path

Finds shortest paths between all pairs of vertices in a weighted graph.
Handles negative edge weights but not negative weight cycles.

Time Complexity:  O(V^3)
Space Complexity: O(V^2)
"""

INF = float('inf')


def floyd_warshall(num_vertices, edges):
    """
    edges: list of (u, v, weight)
    Returns: dist matrix where dist[i][j] = shortest path from i to j
    """
    dist = [[INF] * num_vertices for _ in range(num_vertices)]

    # Distance from a vertex to itself is 0
    for i in range(num_vertices):
        dist[i][i] = 0

    # Initialize with direct edges
    for u, v, w in edges:
        dist[u][v] = w

    # Relax through each intermediate vertex
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if dist[i][k] != INF and dist[k][j] != INF:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


def print_solution(dist):
    n = len(dist)
    print("Shortest distance matrix:")
    header = "     " + "  ".join(f"{j:4}" for j in range(n))
    print(header)
    for i in range(n):
        row = f"{i:3}: " + "  ".join(f"{dist[i][j]:4}" if dist[i][j] != INF else " INF" for j in range(n))
        print(row)


if __name__ == "__main__":
    edges = [
        (0, 1, 3),
        (0, 3, 7),
        (1, 0, 8),
        (1, 2, 2),
        (2, 0, 5),
        (2, 3, 1),
        (3, 0, 2),
    ]
    dist = floyd_warshall(4, edges)
    print_solution(dist)

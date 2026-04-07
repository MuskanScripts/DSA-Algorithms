"""
Dijkstra's Algorithm — Shortest Path in Weighted Graphs

Finds the shortest path from a source vertex to all other vertices
in a graph with non-negative edge weights.

Time Complexity:  O((V + E) log V) with a min-heap
Space Complexity: O(V)
"""

import heapq
from collections import defaultdict


def dijkstra(graph, source, num_vertices):
    """
    graph: dict of {node: [(neighbor, weight), ...]}
    Returns: dist array where dist[i] = shortest distance from source to i
    """
    dist = [float('inf')] * num_vertices
    dist[source] = 0
    min_heap = [(0, source)]  # (distance, node)

    while min_heap:
        d, u = heapq.heappop(min_heap)
        if d > dist[u]:
            continue
        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(min_heap, (dist[v], v))

    return dist


if __name__ == "__main__":
    # Build adjacency list for an undirected weighted graph
    graph = defaultdict(list)
    edges = [
        (0, 1, 4), (0, 2, 1),
        (2, 1, 2), (1, 3, 1),
        (2, 3, 5), (3, 4, 3),
    ]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    source = 0
    distances = dijkstra(graph, source, num_vertices=5)
    print(f"Shortest distances from node {source}:")
    for i, d in enumerate(distances):
        print(f"  Node {i}: {d}")

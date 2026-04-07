"""
Minimum Spanning Tree — Prim's Algorithm

Grows the MST one edge at a time, always adding the minimum weight
edge connecting a visited vertex to an unvisited vertex.

Time Complexity:  O((V + E) log V) with a min-heap
Space Complexity: O(V)
"""

import heapq
from collections import defaultdict


def prim(num_vertices, edges):
    """
    edges: list of (u, v, weight)
    Returns: (MST edges list, total weight)
    """
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((w, v))
        graph[v].append((w, u))

    visited = set()
    min_heap = [(0, 0, -1)]  # (weight, node, parent)
    mst = []
    total_weight = 0

    while min_heap and len(visited) < num_vertices:
        weight, node, parent = heapq.heappop(min_heap)
        if node in visited:
            continue
        visited.add(node)
        if parent != -1:
            mst.append((parent, node, weight))
            total_weight += weight
        for edge_weight, neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor, node))

    return mst, total_weight


if __name__ == "__main__":
    edges = [
        (0, 1, 2), (0, 3, 6),
        (1, 2, 3), (1, 3, 8), (1, 4, 5),
        (2, 4, 7),
        (3, 4, 9),
    ]
    mst, total = prim(5, edges)
    print("Prim's MST edges (u, v, weight):")
    for u, v, w in mst:
        print(f"  {u} -- {v}  weight: {w}")
    print(f"Total MST weight: {total}")

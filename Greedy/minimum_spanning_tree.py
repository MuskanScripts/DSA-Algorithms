"""
Minimum Spanning Tree — Greedy Approach Summary

Both Kruskal's and Prim's algorithms are greedy algorithms
for finding the Minimum Spanning Tree (MST) of a connected,
undirected, weighted graph.

This file demonstrates both in a unified interface.
See also: ../Graphs/kruskal.py and ../Graphs/prim.py for
full standalone implementations.

Time Complexity:
    Kruskal: O(E log E)
    Prim:    O((V + E) log V)
"""

import heapq
from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        return True


def kruskal_mst(num_vertices, edges):
    uf = UnionFind(num_vertices)
    mst, total = [], 0
    for w, u, v in sorted(edges):
        if uf.union(u, v):
            mst.append((u, v, w))
            total += w
    return mst, total


def prim_mst(num_vertices, edges):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((w, v))
        graph[v].append((w, u))

    visited = set()
    heap = [(0, 0, -1)]
    mst, total = [], 0

    while heap and len(visited) < num_vertices:
        w, node, parent = heapq.heappop(heap)
        if node in visited:
            continue
        visited.add(node)
        if parent != -1:
            mst.append((parent, node, w))
            total += w
        for ew, neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(heap, (ew, neighbor, node))

    return mst, total


if __name__ == "__main__":
    # (u, v, weight)
    raw_edges = [(0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (1, 4, 5), (2, 4, 7), (3, 4, 9)]
    weighted_edges = [(w, u, v) for u, v, w in raw_edges]

    mst_k, total_k = kruskal_mst(5, weighted_edges)
    print("Kruskal's MST:")
    for u, v, w in mst_k:
        print(f"  {u} -- {v}  weight: {w}")
    print(f"  Total weight: {total_k}")

    mst_p, total_p = prim_mst(5, raw_edges)
    print("\nPrim's MST:")
    for u, v, w in mst_p:
        print(f"  {u} -- {v}  weight: {w}")
    print(f"  Total weight: {total_p}")

"""
Minimum Spanning Tree — Kruskal's Algorithm

Finds a spanning tree of minimum total edge weight using a
Union-Find (Disjoint Set Union) data structure.

Time Complexity:  O(E log E)
Space Complexity: O(V)
"""


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        # Union by rank
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        return True


def kruskal(num_vertices, edges):
    """
    edges: list of (weight, u, v)
    Returns: (MST edges list, total weight)
    """
    edges_sorted = sorted(edges)
    uf = UnionFind(num_vertices)
    mst = []
    total_weight = 0

    for weight, u, v in edges_sorted:
        if uf.union(u, v):
            mst.append((u, v, weight))
            total_weight += weight
            if len(mst) == num_vertices - 1:
                break

    return mst, total_weight


if __name__ == "__main__":
    # (weight, u, v)
    edges = [
        (10, 0, 1), (6, 0, 2), (5, 0, 3),
        (15, 1, 3), (4, 2, 3),
    ]
    mst, total = kruskal(4, edges)
    print("Kruskal's MST edges (u, v, weight):")
    for u, v, w in mst:
        print(f"  {u} -- {v}  weight: {w}")
    print(f"Total MST weight: {total}")

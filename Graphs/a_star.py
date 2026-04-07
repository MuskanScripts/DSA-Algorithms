"""
A* Search Algorithm — Heuristic Shortest Path

Finds the shortest path from start to goal using a heuristic function
to guide the search. Combines Dijkstra's correctness with greedy
best-first search efficiency.

Time Complexity:  O(E) in the best case, O(b^d) worst case
Space Complexity: O(V)
"""

import heapq


def heuristic(a, b):
    """Manhattan distance heuristic for grid-based problems."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def a_star(grid, start, goal):
    """
    grid: 2D list where 0 = passable, 1 = blocked
    start, goal: (row, col) tuples
    Returns: list of (row, col) coordinates forming the path, or []
    """
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    open_set = [(0, start)]
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return list(reversed(path))

        r, c = current
        for dr, dc in directions:
            neighbor = (r + dr, c + dc)
            nr, nc = neighbor
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                tentative_g = g_score[current] + 1
                if tentative_g < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = tentative_g + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return []  # No path found


if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 1],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
    ]
    start = (0, 0)
    goal = (4, 4)
    path = a_star(grid, start, goal)
    print(f"Path from {start} to {goal}:")
    if path:
        print(" -> ".join(str(p) for p in path))
    else:
        print("No path found")

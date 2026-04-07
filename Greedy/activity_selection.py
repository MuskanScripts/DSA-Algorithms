"""
Activity Selection Problem — Greedy Algorithm

Select the maximum number of activities that can be performed
by a single person, given that each activity has a start and
finish time, and a person can only work on one activity at a time.

Time Complexity:  O(n log n) — due to sorting
Space Complexity: O(1)
"""


def activity_selection(activities):
    """
    activities: list of (start, finish) tuples
    Returns: list of selected activities
    """
    sorted_activities = sorted(activities, key=lambda x: x[1])
    selected = [sorted_activities[0]]
    last_finish = sorted_activities[0][1]

    for start, finish in sorted_activities[1:]:
        if start >= last_finish:
            selected.append((start, finish))
            last_finish = finish

    return selected


if __name__ == "__main__":
    activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
    selected = activity_selection(activities)
    print(f"All activities (start, finish): {activities}")
    print(f"Selected activities:            {selected}")
    print(f"Count: {len(selected)}")

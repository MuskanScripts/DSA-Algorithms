"""
Lowest Common Ancestor (LCA) — Binary Tree

Find the lowest (deepest) node that is an ancestor of
both node p and node q in a binary tree.

Approach 1 — Recursive DFS: O(n) time, O(h) space
Approach 2 — Path-based:    O(n) time, O(n) space
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lca(root, p, q):
    """
    Recursive approach.
    Works for any binary tree (not just BST).
    """
    if root is None or root.val == p or root.val == q:
        return root

    left = lca(root.left, p, q)
    right = lca(root.right, p, q)

    if left and right:
        return root   # p and q are in different subtrees
    return left if left else right


def lca_bst(root, p, q):
    """
    Optimized LCA for a Binary Search Tree.
    Time: O(h), Space: O(1)
    """
    node = root
    while node:
        if p < node.val and q < node.val:
            node = node.left
        elif p > node.val and q > node.val:
            node = node.right
        else:
            return node
    return None


def build_sample_tree():
    r"""
             3
           /   \
          5     1
         / \   / \
        6   2 0   8
           / \
          7   4
    """
    root = TreeNode(3)
    root.left = TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4)))
    root.right = TreeNode(1, TreeNode(0), TreeNode(8))
    return root


if __name__ == "__main__":
    root = build_sample_tree()

    p, q = 5, 1
    result = lca(root, p, q)
    print(f"LCA of {p} and {q}: {result.val}")  # Expected: 3

    p, q = 5, 4
    result = lca(root, p, q)
    print(f"LCA of {p} and {q}: {result.val}")  # Expected: 5

    p, q = 6, 4
    result = lca(root, p, q)
    print(f"LCA of {p} and {q}: {result.val}")  # Expected: 5

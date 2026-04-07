"""
Tree Traversals — In-order, Pre-order, Post-order, Level-order

Demonstrates all four standard traversals on a binary tree.

Time Complexity:  O(n) for all traversals
Space Complexity: O(h) where h is the height (O(n) worst case)
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder(root):
    """Left -> Root -> Right"""
    result = []
    def _inorder(node):
        if node:
            _inorder(node.left)
            result.append(node.val)
            _inorder(node.right)
    _inorder(root)
    return result


def preorder(root):
    """Root -> Left -> Right"""
    result = []
    def _preorder(node):
        if node:
            result.append(node.val)
            _preorder(node.left)
            _preorder(node.right)
    _preorder(root)
    return result


def postorder(root):
    """Left -> Right -> Root"""
    result = []
    def _postorder(node):
        if node:
            _postorder(node.left)
            _postorder(node.right)
            result.append(node.val)
    _postorder(root)
    return result


def level_order(root):
    """Breadth-first traversal level by level."""
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result


def build_sample_tree():
    r"""
         1
        / \
       2   3
      / \   \
     4   5   6
    """
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(4), TreeNode(5))
    root.right = TreeNode(3, None, TreeNode(6))
    return root


if __name__ == "__main__":
    root = build_sample_tree()
    print("In-order   (L-Root-R):", inorder(root))
    print("Pre-order  (Root-L-R):", preorder(root))
    print("Post-order (L-R-Root):", postorder(root))
    print("Level-order (BFS):    ", level_order(root))

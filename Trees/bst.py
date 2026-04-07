"""
Binary Search Tree (BST) — Insert, Delete, Search

A BST maintains the property:
    left child < node < right child

Operations:
    insert  — O(h) average O(log n), worst O(n)
    search  — O(h) average O(log n), worst O(n)
    delete  — O(h) average O(log n), worst O(n)
    inorder — O(n)
"""


class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # ------------------------------------------------------------------
    # Insert
    # ------------------------------------------------------------------
    def insert(self, val):
        self.root = self._insert(self.root, val)

    def _insert(self, node, val):
        if node is None:
            return BSTNode(val)
        if val < node.val:
            node.left = self._insert(node.left, val)
        elif val > node.val:
            node.right = self._insert(node.right, val)
        return node  # duplicate values are ignored

    # ------------------------------------------------------------------
    # Search
    # ------------------------------------------------------------------
    def search(self, val):
        return self._search(self.root, val)

    def _search(self, node, val):
        if node is None:
            return False
        if val == node.val:
            return True
        if val < node.val:
            return self._search(node.left, val)
        return self._search(node.right, val)

    # ------------------------------------------------------------------
    # Delete
    # ------------------------------------------------------------------
    def delete(self, val):
        self.root = self._delete(self.root, val)

    def _delete(self, node, val):
        if node is None:
            return None
        if val < node.val:
            node.left = self._delete(node.left, val)
        elif val > node.val:
            node.right = self._delete(node.right, val)
        else:
            # Node to delete found
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            # Node has two children: replace with in-order successor
            successor = self._min_node(node.right)
            node.val = successor.val
            node.right = self._delete(node.right, successor.val)
        return node

    def _min_node(self, node):
        while node.left:
            node = node.left
        return node

    # ------------------------------------------------------------------
    # In-order traversal (returns sorted list)
    # ------------------------------------------------------------------
    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.val)
            self._inorder(node.right, result)


if __name__ == "__main__":
    bst = BST()
    values = [5, 3, 7, 1, 4, 6, 8]
    for v in values:
        bst.insert(v)

    print("In-order after inserts:", bst.inorder())
    print("Search 4:", bst.search(4))
    print("Search 9:", bst.search(9))

    bst.delete(3)
    print("In-order after deleting 3:", bst.inorder())

    bst.delete(5)
    print("In-order after deleting root (5):", bst.inorder())

"""
AVL Tree — Self-Balancing Binary Search Tree

An AVL tree maintains the height-balance property:
    |height(left) - height(right)| <= 1 for every node.

After each insert or delete, the tree rebalances via rotations.

Operations:
    insert  — O(log n)
    delete  — O(log n)
    search  — O(log n)
"""


class AVLNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------
    def _height(self, node):
        return node.height if node else 0

    def _balance_factor(self, node):
        return self._height(node.left) - self._height(node.right) if node else 0

    def _update_height(self, node):
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    # ------------------------------------------------------------------
    # Rotations
    # ------------------------------------------------------------------
    def _rotate_right(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        self._update_height(z)
        self._update_height(y)
        return y

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        self._update_height(z)
        self._update_height(y)
        return y

    def _rebalance(self, node):
        self._update_height(node)
        bf = self._balance_factor(node)

        # Left heavy
        if bf > 1:
            if self._balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)  # Left-Right case
            return self._rotate_right(node)

        # Right heavy
        if bf < -1:
            if self._balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)  # Right-Left case
            return self._rotate_left(node)

        return node

    # ------------------------------------------------------------------
    # Insert
    # ------------------------------------------------------------------
    def __init__(self):
        self.root = None

    def insert(self, val):
        self.root = self._insert(self.root, val)

    def _insert(self, node, val):
        if node is None:
            return AVLNode(val)
        if val < node.val:
            node.left = self._insert(node.left, val)
        elif val > node.val:
            node.right = self._insert(node.right, val)
        else:
            return node  # duplicates ignored
        return self._rebalance(node)

    # ------------------------------------------------------------------
    # Delete
    # ------------------------------------------------------------------
    def delete(self, val):
        self.root = self._delete(self.root, val)

    def _min_node(self, node):
        while node.left:
            node = node.left
        return node

    def _delete(self, node, val):
        if node is None:
            return None
        if val < node.val:
            node.left = self._delete(node.left, val)
        elif val > node.val:
            node.right = self._delete(node.right, val)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            successor = self._min_node(node.right)
            node.val = successor.val
            node.right = self._delete(node.right, successor.val)
        return self._rebalance(node)

    # ------------------------------------------------------------------
    # Search
    # ------------------------------------------------------------------
    def search(self, val):
        node = self.root
        while node:
            if val == node.val:
                return True
            node = node.left if val < node.val else node.right
        return False

    # ------------------------------------------------------------------
    # In-order traversal
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
    avl = AVLTree()
    values = [10, 20, 30, 40, 50, 25]
    for v in values:
        avl.insert(v)

    print("In-order after inserts:", avl.inorder())
    print("Height of root:", avl.root.height)
    print("Search 25:", avl.search(25))
    print("Search 99:", avl.search(99))

    avl.delete(40)
    print("In-order after deleting 40:", avl.inorder())

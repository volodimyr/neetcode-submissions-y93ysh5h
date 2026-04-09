class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.arr = []
        self.cursor = 0
        self._inorder(root)

    def _inorder(self, node: Optional[TreeNode]):
        if not node:
            return
        self._inorder(node.left)
        self.arr.append(node.val)
        self._inorder(node.right)

    def next(self) -> int:
        v = self.arr[self.cursor]
        self.cursor += 1
        return v

    def hasNext(self) -> bool:
        return self.cursor < len(self.arr)

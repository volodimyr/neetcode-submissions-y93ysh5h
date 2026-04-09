class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.root = root
        cur = root
        while cur:
            self.stack.append(cur)
            cur = cur.left

    def next(self) -> int:
        pop = self.stack.pop()
        cur = pop.right
        while cur:
            self.stack.append(cur)
            cur = cur.left
        return pop.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0
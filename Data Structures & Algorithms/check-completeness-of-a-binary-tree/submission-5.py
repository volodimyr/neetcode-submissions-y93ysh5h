
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        completed = False
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node:
                if completed:
                    return False
                q.append(node.left)
                q.append(node.right)
            else:
                completed = True
                
        return True
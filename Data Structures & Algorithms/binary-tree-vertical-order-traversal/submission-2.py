# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        m = defaultdict(list)
        q = deque()
        q.append((root, 0))

        while q:
            pop, group  = q.popleft()
            m[group].append(pop.val)
            if pop.left:
                q.append((pop.left, group-1))
            if pop.right:
                q.append((pop.right, group+1))
        
        return [m[c] for c in sorted(m)]

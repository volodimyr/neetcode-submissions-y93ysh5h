# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        
        x = set()
        def dfs(root):
            if not root:
                return
            x.add(target - root.val)
            dfs(root.left)
            dfs(root.right)
        
        dfs(root1)

        def search(root):
            if not root:
                return False
            
            if root.val in x:
                return True
            if search(root.left):
                return True
            if search(root.right):
                return True
            return False
        
        return search(root2)
            
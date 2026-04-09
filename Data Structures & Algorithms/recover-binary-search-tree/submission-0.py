# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        arr = []
        def inorder(root):
            if not root:
                return
            
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)
        
        inorder(root)
        arr.sort()

        i = 0
        def dfs(root):
            nonlocal i
            if not root:
                return
            dfs(root.left)
            root.val = arr[i]
            i += 1
            dfs(root.right)
        
        dfs(root)

        
        
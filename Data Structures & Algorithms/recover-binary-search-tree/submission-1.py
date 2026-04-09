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
            arr.append(root)
            inorder(root.right)

        inorder(root)

        vals = sorted(node.val for node in arr)

        for i in range(len(arr)):
            arr[i].val = vals[i]

        
        
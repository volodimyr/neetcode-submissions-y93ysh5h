class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        cur = 0
        return self.track(root, cur, targetSum)
    
    def track(self, root: Optional[TreeNode], cur: int, t: int) -> bool:
        if not root:
            return False
        
        cur += root.val
        if not root.left and not root.right and cur == t:
            return True
        if self.track(root.left, cur, t):
            return True
        if self.track(root.right, cur, t):
            return True
        
        return False

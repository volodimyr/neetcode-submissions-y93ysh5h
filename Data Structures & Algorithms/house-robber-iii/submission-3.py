class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        cache = {}
        def dfs(root, taken):
            if not root:
                return 0
            if (root, taken) in cache:
                return cache[(root, taken)]
            res = 0
            if taken:
                res = dfs(root.left, False) + dfs(root.right, False)
            else:
                skip = dfs(root.left, False) + dfs(root.right, False)
                add = root.val + dfs(root.left, True) + dfs(root.right, True)
                res = max(skip, add)
            cache[(root,taken)] = res
            return res
            
        return dfs(root, False)
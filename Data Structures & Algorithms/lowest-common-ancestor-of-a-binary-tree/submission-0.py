class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def path(root, search, p):
            if not root:
                return False
            p.append(root)
            if root.val == search:
                return True
            if path(root.left, search, p):
                return True
            if path(root.right, search, p):
                return True
            p.pop()
            return False
        
        ppath = []
        path(root, p.val, ppath)
        qpath = []
        path(root, q.val, qpath)

        i, j = 0, 0
        parent = None
        while i < len(ppath) and j < len(qpath) and ppath[i].val == qpath[j].val:
            parent = ppath[i]
            i+=1
            j+=1

        return parent

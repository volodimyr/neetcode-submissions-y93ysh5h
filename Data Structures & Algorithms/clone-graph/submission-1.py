class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        clones = {node.val: Node(node.val)}
        q = deque([node])
        while q:
            cur = q.popleft()
            for n in cur.neighbors:
                if n.val not in clones:
                    clones[n.val] = Node(n.val)
                    q.append(n)
                clones[cur.val].neighbors.append(clones[n.val])

        return clones[node.val]
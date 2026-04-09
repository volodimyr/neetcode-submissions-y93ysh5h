func deleteNode(root *TreeNode, key int) *TreeNode {
	if root == nil {
		return root
	}
	var parent *TreeNode
	cur := root
	for cur != nil && cur.Val != key {
		parent = cur
		if cur.Val > key {
			cur = cur.Left
		} else {
			cur = cur.Right
		}
	}
	if cur == nil {
		return root
	}

	successor := successor(cur)
	if parent == nil {
		return successor
	}

	if parent.Left == cur {
		parent.Left = successor
	} else {
		parent.Right = successor
	}

	return root
}

func successor(root *TreeNode) *TreeNode {
	if root.Right == nil {
		return root.Left
	}
	if root.Left == nil {
		return root.Right
	}
	parent := root
	successor := root.Right
	for successor.Left != nil {
		parent = successor
		successor = successor.Left
	}
	if parent == root {
		successor.Left = root.Left
		return successor
	}
	parent.Left = successor.Right
	successor.Left = root.Left
	successor.Right = root.Right

	return successor
}

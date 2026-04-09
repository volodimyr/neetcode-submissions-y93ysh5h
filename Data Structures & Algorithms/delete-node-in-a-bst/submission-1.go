func deleteNode(root *TreeNode, key int) *TreeNode {
	if root == nil {
		return root
	}

	if root.Val > key {
		root.Left = deleteNode(root.Left, key)
	} else if root.Val < key {
		root.Right = deleteNode(root.Right, key)
	} else {
		if root.Left == nil {
			return root.Right
		}
		if root.Right == nil {
			return root.Left
		}
		root.Val = successor(root.Right, root)
	}

	return root

}

func successor(node *TreeNode, parent *TreeNode) int {
	if node.Left == nil {
		val := node.Val

		if parent.Right == node {
			parent.Right = node.Right
		} else {
			parent.Left = node.Right
		}
		return val
	}
	return successor(node.Left, node)
}
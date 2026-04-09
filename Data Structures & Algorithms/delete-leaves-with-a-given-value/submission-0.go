func removeLeafNodes(root *TreeNode, target int) *TreeNode {
	return traversal(root, target)
}

func traversal(root *TreeNode, target int) *TreeNode {
	if root == nil {
		return nil
	}
	if root.Left == nil && root.Right == nil && root.Val == target {
		return nil
	}
	root.Left = traversal(root.Left, target)
	root.Right = traversal(root.Right, target)
	if root.Left == nil && root.Right == nil && root.Val == target {
		return nil
	}
	return root
}

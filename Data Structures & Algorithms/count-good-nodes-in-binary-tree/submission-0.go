func goodNodes(root *TreeNode) int {
	return traversal(root, root.Val)
}

func traversal(root *TreeNode, max int) int {
	if root == nil {
		return 0
	}
	var count int
	if root.Val >= max {
		max = root.Val
		count = 1
	}
	cleft := traversal(root.Left, max)
	cright := traversal(root.Right, max)
	return count + cleft + cright
}
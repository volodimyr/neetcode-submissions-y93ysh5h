func isBalanced(root *TreeNode) bool {
	if root == nil {
		return true
	}
	left, right := height(root.Left), height(root.Right)
	if left > right && left-right > 1 {
		return false
	} else if right-left > 1 {
		return false
	}

	return isBalanced(root.Left) && isBalanced(root.Right)
}

func height(root *TreeNode) int {
	if root == nil {
		return 0
	}
	return max(height(root.Left), height(root.Right)) + 1
}
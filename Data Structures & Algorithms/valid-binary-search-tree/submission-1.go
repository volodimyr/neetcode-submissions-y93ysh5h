func isValidBST(root *TreeNode) bool {
	return valid(root, nil, nil)
}

func valid(root *TreeNode, min, max *int) bool {
	if root == nil {
		return true
	}
	if min != nil && root.Val <= *min {
		return false
	}
	if max != nil && root.Val >= *max {
		return false
	}

	return valid(root.Left, min, &root.Val) && valid(root.Right, &root.Val, max)
}
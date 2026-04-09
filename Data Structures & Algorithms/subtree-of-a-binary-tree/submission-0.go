func isSubtree(root *TreeNode, subRoot *TreeNode) bool {
	if root == nil {
		return false
	}
	if root.Val == subRoot.Val && equal(root, subRoot) {
		return true
	}
	return isSubtree(root.Left, subRoot) || isSubtree(root.Right, subRoot)
}

func equal(subRoot0, subRoot *TreeNode) bool {
	if subRoot0 == nil && subRoot == nil {
		return true
	}
	if subRoot0 == nil || subRoot == nil {
		return false
	}
	if subRoot0.Val != subRoot.Val {
		return false
	}
	return equal(subRoot0.Left, subRoot.Left) && equal(subRoot0.Right, subRoot.Right)
}
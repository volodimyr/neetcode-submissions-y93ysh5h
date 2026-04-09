func maxDepth(root *TreeNode) int {
    if root == nil {
        return 0
    }
	deepest := 1
	traverse(root, 1, &deepest)
	return deepest
}

func traverse(root *TreeNode, d int, deepest *int) {
	if root == nil {
		return
	}
	if d >= *deepest {
		*deepest = d
	}
	traverse(root.Left, d+1, deepest)
	traverse(root.Right, d+1, deepest)
}
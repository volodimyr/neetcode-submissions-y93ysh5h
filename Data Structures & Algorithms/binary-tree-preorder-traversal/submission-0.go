func preorderTraversal(root *TreeNode) []int {
	arr := []int{}
	traversal(root, &arr)
	return arr
}

func traversal(root *TreeNode, arr *[]int) {
	if root == nil {
		return
	}
	*arr = append(*arr, root.Val)
	traversal(root.Left, arr)
	traversal(root.Right, arr)
}

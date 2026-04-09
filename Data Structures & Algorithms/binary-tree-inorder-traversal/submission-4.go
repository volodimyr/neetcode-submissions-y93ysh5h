func inorderTraversal(root *TreeNode) []int {
	arr := []int{}
	traversal(root, &arr)
	return arr
}

func traversal(root *TreeNode, arr *[]int) {
	if root == nil {
		return 
	}
	traversal(root.Left, arr)
	*arr = append(*arr, root.Val)
	traversal(root.Right, arr)
}
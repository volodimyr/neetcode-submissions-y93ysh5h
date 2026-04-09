/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func postorderTraversal(root *TreeNode) []int {
	arr := []int{}
	traversal(root, &arr)
	return arr
}

func traversal(root *TreeNode, arr *[]int) {
	if root == nil {
		return
	}

	traversal(root.Left, arr)
	traversal(root.Right, arr)
	*arr = append(*arr, root.Val)
}
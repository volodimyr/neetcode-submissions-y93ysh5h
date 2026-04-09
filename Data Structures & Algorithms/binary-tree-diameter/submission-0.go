/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func diameterOfBinaryTree(root *TreeNode) int {
	var max int
	diameter(root, &max)
	return max
}

func diameter(root *TreeNode, m *int) int {
	if root == nil {
		return 0
	}
	left := diameter(root.Left, m)
	right := diameter(root.Right, m)
	*m = max(*m, left+right)
	return max(left, right) + 1
}

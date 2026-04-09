/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func kthSmallest(root *TreeNode, k int) int {
    arr := []int{}
    traversal(root, &arr)
    return arr[k-1]
}

func traversal(root *TreeNode, arr *[]int) {
    if root == nil{
        return
    }
    traversal(root.Left, arr)
    *arr = append(*arr, root.Val)
    traversal(root.Right, arr)
}

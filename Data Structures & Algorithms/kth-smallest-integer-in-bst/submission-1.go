/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func kthSmallest(root *TreeNode, k int) int {
    sm := -1
    find(root, &k, &sm)
    return sm
}

func find(root *TreeNode, k *int, sm *int)  {
    if root == nil{
        return
    }
    find(root.Left, k, sm)
    if *k > 0 {
        *sm = root.Val
        *k--
    }
    find(root.Right, k, sm)
    return 
}

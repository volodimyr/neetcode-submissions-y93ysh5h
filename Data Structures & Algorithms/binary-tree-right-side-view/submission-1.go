/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func rightSideView(root *TreeNode) []int {
    arr := []int{}
    if root == nil {
        return arr
    }
    q := []*TreeNode{root}

    for len(q) != 0 {
        qlen := len(q)
        mostRight := q[0]
        arr = append(arr, mostRight.Val)
        for _, node := range q {
            if node.Right != nil {
                q = append(q, node.Right)
            }
            if node.Left != nil {
                q= append(q, node.Left)
            }
        }
        q = q[qlen:]
    }
    return arr
}

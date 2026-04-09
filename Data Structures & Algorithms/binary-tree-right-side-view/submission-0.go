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
        mostRight := q[qlen-1]
        arr = append(arr, mostRight.Val)
        for _, node := range q {
            if node.Left != nil {
                q = append(q, node.Left)
            }
            if node.Right != nil {
                q= append(q, node.Right)
            }
        }
        q = q[qlen:]
    }
    return arr
}

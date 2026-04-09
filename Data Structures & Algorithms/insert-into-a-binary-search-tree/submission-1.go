/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func insertIntoBST(root *TreeNode, val int) *TreeNode {
    if root == nil {
        root = &TreeNode{Val:val}
        return root
    }
    cur := root

    for {
        if cur.Val > val {
            if cur.Left == nil {
                cur.Left= &TreeNode{Val:val}
                break
            }else {
                cur = cur.Left
            }
        }else {
            if cur.Right == nil {
                cur.Right = &TreeNode{Val:val}
                break
            }else {
                cur = cur.Right
            }
        }
    }

    return root
}

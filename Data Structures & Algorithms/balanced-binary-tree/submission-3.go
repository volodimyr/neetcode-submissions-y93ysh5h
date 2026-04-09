func isBalanced(root *TreeNode) bool {
	return height(root) != -1
}

func height(root *TreeNode) int {
    if root == nil {
        return 0
    }
    left := height(root.Left)
    if left == -1 {
        return left
    }
    right := height(root.Right)
    if right ==-1 {
        return right
    }
    if abs(right-left) > 1 {
        return -1
    }
    return max(right, left)+1
}

func abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}

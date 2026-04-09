func levelOrder(root *TreeNode) [][]int {
	var lvl int
	arr := [][]int{}
	if root == nil {
		return arr
	}
	q := []*TreeNode{root}

	for len(q) != 0 {
		arr = append(arr, make([]int, len(q)))
		for i := range len(q) {
			tn := q[0]
			q = q[1:]
			arr[lvl][i] = tn.Val
			if tn.Left != nil {
				q = append(q, tn.Left)
			}
			if tn.Right != nil {
				q = append(q, tn.Right)
			}
		}
		lvl++
	}
	return arr
}
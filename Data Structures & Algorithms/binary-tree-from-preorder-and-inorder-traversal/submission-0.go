func buildTree(preorder []int, inorder []int) *TreeNode {

	/*
		      3
		   /     \
		  9      20
		 / \    /  \
		2  11 15   7
	*/
	//	preorder := []int{3, 9, 2, 11, 20, 15, 7}
	// inorder := []int{2, 9, 11, 3, 15, 20, 7}

	m := make(map[int]int, len(inorder))
	for i, n := range inorder {
		m[n] = i
	}
	return build(m, preorder, inorder)
}

func build(m map[int]int, preorder []int, inorder []int) *TreeNode {
	if len(preorder) == 0 {
		return nil
	}
	root := &TreeNode{Val: preorder[0]}
	split := m[root.Val]
	if split != 0 {
		root.Left = buildTree(preorder[1:split+1], inorder[:split])
	}
	if len(preorder) > split {
		root.Right = buildTree(preorder[split+1:], inorder[split+1:])
	}
	return root
}
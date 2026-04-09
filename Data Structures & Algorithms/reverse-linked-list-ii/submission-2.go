func reverseBetween(head *ListNode, left int, right int) *ListNode {
	if left == right {
		return head
	}

	dummy := &ListNode{Next: head}
	prev := dummy

	for i := 1; i < left; i++ {
		prev = prev.Next
	}

	cur := prev.Next
	for i := 0; i < right-left; i++ {
		next := cur.Next
		cur.Next = next.Next
		next.Next = prev.Next
		prev.Next = next
	}

	return dummy.Next
}
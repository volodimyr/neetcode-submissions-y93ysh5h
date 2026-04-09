func insertionSortList(head *ListNode) *ListNode {
	if head == nil {
		return head
	}
	dummy := &ListNode{Next: head}
	curr := head.Next
	head.Next = nil
	for curr != nil {
		next := curr.Next
		prev := dummy
		for prev.Next != nil && prev.Next.Val < curr.Val {
			prev = prev.Next
		}
		curr.Next, prev.Next = prev.Next, curr
		curr = next

	}
	return dummy.Next
}

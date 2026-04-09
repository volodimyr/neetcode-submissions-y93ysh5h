func reorderList(head *ListNode) {
	slow := head
	fast := head
	for fast != nil && fast.Next != nil {
		fast = fast.Next.Next
		slow = slow.Next
	}

	secondHalf := slow.Next
	slow.Next = nil
	// reverse secondhalf
	var prev *ListNode
	curr := secondHalf
	for curr != nil {
		next := curr.Next
		curr.Next = prev
		prev = curr
		curr = next
	}
	secondHalf = prev

	merge(head, secondHalf, true)
}

func merge(list1, list2 *ListNode, takeFirst bool) *ListNode {
	if list1 == nil {
		return list2
	}
	if list2 == nil {
		return list1
	}
	if takeFirst {
		list1.Next = merge(list1.Next, list2, false)
		return list1
	} else {
		list2.Next = merge(list1, list2.Next, true)
		return list2
	}
}

func reverse(head *ListNode) *ListNode {
	if head == nil {
		return head
	}
	if head.Next == nil {
		return head
	}
	nhead := reverse(head.Next)
	head.Next.Next = head
	head.Next = nil
	return nhead
}
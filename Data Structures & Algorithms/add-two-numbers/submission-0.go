func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	cur1 := l1
	prev := cur1
	cur2 := l2
	var carry int
	for {
		sum := carry
		if cur1 == nil && cur2 == nil {
			if carry != 0 {
				prev.Next = &ListNode{Val: carry}
			}
			break
		}
		if cur1 != nil {
			sum += cur1.Val
		}
		if cur2 != nil {
			sum += cur2.Val
		}

		if cur1 != nil {
			cur1.Val = sum % 10
		} else {
			cur2.Val = sum % 10
			prev.Next = cur2
			prev = prev.Next
		}

		if cur1 != nil {
			prev = cur1
			cur1 = cur1.Next
		}
		if cur2 != nil {
			cur2 = cur2.Next
		}
		carry = sum / 10
	}

	return l1
}
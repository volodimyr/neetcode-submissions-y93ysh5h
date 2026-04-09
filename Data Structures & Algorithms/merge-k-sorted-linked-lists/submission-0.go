func mergeKLists(lists []*ListNode) *ListNode {
	if len(lists) < 1 {
		return nil
	}
	if len(lists) == 1 {
		return lists[0]
	}

	return mergeRange(lists, 0, len(lists)-1)
}

func mergeRange(lists []*ListNode, L, R int) *ListNode {
	if L == R {
		return lists[L]
	}
	mid := (L + R) / 2
	left := mergeRange(lists, L, mid)
	right := mergeRange(lists, mid+1, R)
	return merge(left, right)
}

func merge(list1, list2 *ListNode) *ListNode {
	dummy := &ListNode{}

	cur := dummy
	cur1 := list1
	cur2 := list2
	for cur1 != nil && cur2 != nil {
		if cur1.Val < cur2.Val {
			cur.Next = cur1
			cur1 = cur1.Next
		} else {
			cur.Next = cur2
			cur2 = cur2.Next
		}
		cur = cur.Next
	}

	if cur1 != nil {
		cur.Next = cur1
	} else if cur2 != nil {
		cur.Next = cur2
	}
	return dummy.Next
}
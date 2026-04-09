/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func reorderList(head *ListNode) {
	slow := head
	fast := head
	for fast != nil && fast.Next != nil {
		fast = fast.Next.Next
		slow = slow.Next
	}
	secondHalf := slow.Next
	slow.Next = nil
	secondHalf = reverse(secondHalf)
	merge(head, secondHalf, 1)
}

func merge(list1, list2 *ListNode, numb int) *ListNode {
	if list1 == nil {
		return list2
	}
	if list2 == nil {
		return list1
	}
	if numb%2 != 0 {
		list1.Next = merge(list1.Next, list2, numb+1)
		return list1
	} else {
		list2.Next = merge(list1, list2.Next, numb+1)
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

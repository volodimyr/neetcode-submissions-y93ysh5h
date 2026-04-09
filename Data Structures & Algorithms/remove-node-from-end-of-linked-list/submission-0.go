/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func removeNthFromEnd(head *ListNode, n int) *ListNode {
	dummy := &ListNode{Next: head}

	l := dummy
	r := head
	for n > 0 {
		r = r.Next
		n--
	}
	for r != nil {
		r = r.Next
		l = l.Next
	}
	l.Next = l.Next.Next

	return dummy.Next
}

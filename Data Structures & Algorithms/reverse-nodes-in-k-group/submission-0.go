/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func reverseKGroup(head *ListNode, k int) *ListNode {
    dummy := &ListNode{}
    cur := head
    dcur := dummy
    for cur != nil {
        dcur.Next, cur = reverse(cur, k)
        for dcur.Next != nil {
            dcur = dcur.Next
        }
    }
    return dummy.Next
}

func reverse(head *ListNode, k int) (*ListNode, *ListNode) {
    check := head
    i := k
    for check != nil && i > 1 {
        check = check.Next
        i--
    }
    if check == nil {
        return head, nil
    }
    var prev *ListNode
    cur := head
    for k > 0 && cur != nil {
        next := cur.Next
        cur.Next = prev
        prev = cur
        cur = next
        k--
    }
    return prev, cur
}
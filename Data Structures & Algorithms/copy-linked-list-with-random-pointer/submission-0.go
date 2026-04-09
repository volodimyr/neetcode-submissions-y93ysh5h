func copyRandomList(head *Node) *Node {
	if head == nil {
		return head
	}
	m := make(map[*Node]*Node)
	for cur := head; cur != nil; cur = cur.Next {
		m[cur] = &Node{Val: cur.Val}
	}

	for cur := head; cur != nil; cur = cur.Next {
		copied := m[cur]
		copied.Next = m[cur.Next]
		copied.Random = m[cur.Random]
	}

	return m[head]
}
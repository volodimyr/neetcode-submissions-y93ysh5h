type LinkedList struct {
	head *node
}

type node struct {
	val  int
	next *node
}

func NewLinkedList() *LinkedList {
	return &LinkedList{}
}

func (ll *LinkedList) Get(index int) int {
	if ll.head == nil {
		return -1
	}
	curr := ll.head
	for i := 0; i < index; i++ {
		if curr == nil {
			return -1
		}
		curr = curr.next
	}
    if curr == nil {
		return -1
	}
	return curr.val
}

func (ll *LinkedList) InsertHead(val int) {
	ll.head = &node{val: val, next: ll.head}
}

func (ll *LinkedList) InsertTail(val int) {
	newTail := &node{val: val}
	if ll.head == nil {
		ll.head = newTail
		return
	}
	curr := ll.head
	for curr.next != nil {
		curr = curr.next
	}
	curr.next = newTail
}

func (ll *LinkedList) Remove(index int) bool {
    if ll.head == nil {
		return false
	}
	if index == 0 {
		ll.head = ll.head.next
		return true
	}

	curr := ll.head
	for i := 0; i < index-1 && curr != nil; i++ {
		curr = curr.next
	}
	if curr == nil || curr.next == nil {
		return false
	}
	curr.next = curr.next.next
	return true
}

func (ll *LinkedList) GetValues() []int {
	var arr []int
	curr := ll.head
	for curr != nil {
		arr = append(arr, curr.val)
		curr = curr.next
	}
	return arr
}

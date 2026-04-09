type LRUCache struct {
	maxCapacity int
	m           map[int]*Dnode
	queue       *DoublyLinkedList
}

func Constructor(capacity int) LRUCache {
	return LRUCache{
		maxCapacity: capacity,
		m:           make(map[int]*Dnode),
		queue:       NewDoublyLinkedList(),
	}
}

func (l *LRUCache) Put(key int, v int) {
	found, ok := l.m[key]
	if ok {
		l.queue.RemoveByRef(found)
		found.SetVal(v)
		l.queue.InsertHeadByRef(found)
		return
	}
	if len(l.m) == l.maxCapacity {
		delete(l.m, l.queue.RemoveTailAndReturnKey())
	}
	l.m[key] = l.queue.InsertHeadWithKey(v, key)
}

func (l *LRUCache) Get(key int) int {
	found, ok := l.m[key]
	if !ok {
		return -1
	}
	l.queue.RemoveByRef(found)
	l.queue.InsertHeadByRef(found)
	return found.Val()
}

type DoublyLinkedList struct {
	head *Dnode
	tail *Dnode
}

type Dnode struct {
	val  int
	key  int
	next *Dnode
	prev *Dnode
}

func (d *Dnode) Val() int {
	return d.val
}

func (d *Dnode) Key() int {
	return d.key
}

func (d *Dnode) SetVal(v int) {
	d.val = v
}



func NewDoublyLinkedList() *DoublyLinkedList {
	return &DoublyLinkedList{}
}


func (d *DoublyLinkedList) RemoveByRef(ref *Dnode) {
	if ref == d.head {
		d.RemoveHead()
		return
	}
	if ref == d.tail {
		d.RemoveTail()
		return
	}
	ref.prev.next = ref.next
	ref.next.prev = ref.prev
}

func (d *DoublyLinkedList) RemoveHead() {
	if d.head == nil {
		return
	}
	if d.head == d.tail {
		d.tail = nil
		d.head = nil
		return
	}
	d.head = d.head.next
	d.head.prev = nil
}

func (d *DoublyLinkedList) RemoveTailAndReturnKey() int {
	if d.tail == nil {
		return -1
	}
	key := d.tail.Key()
	d.RemoveTail()
	return key
}

func (d *DoublyLinkedList) RemoveTail() {
	if d.tail == nil {
		return
	}
	if d.tail == d.head {
		d.tail = nil
		d.head = nil
		return
	}
	d.tail = d.tail.prev
	d.tail.next = nil
}

func (d *DoublyLinkedList) InsertHeadWithKey(val, key int) *Dnode {
	node := &Dnode{val: val, key: key, prev: nil, next: d.head}
	if d.head != nil {
		d.head.prev = node
	} else {
		d.tail = node
	}
	d.head = node
	return d.head
}


func (d *DoublyLinkedList) InsertHeadByRef(node *Dnode) {
	if d.head != nil {
		d.head.prev, node.next = node, d.head
	} else {
		d.tail = node
	}
	d.head = node
}
type LFUCache struct {
	maxCapacity int
	minFreq     int
	nodes       map[int]*Dnode
	freqList    map[int]*DoublyLinkedList
}

func Constructor(cap int) LFUCache {
	return LFUCache{
		maxCapacity: cap,
		nodes:       make(map[int]*Dnode),
		freqList:    make(map[int]*DoublyLinkedList),
	}
}

func (c *LFUCache) Get(k int) int {
	node, ok := c.nodes[k]
	if !ok {
		return -1
	}
	c.increaseFreq(node)
	return node.Val()
}

func (c *LFUCache) Put(k int, v int) {
	if node, ok := c.nodes[k]; ok {
		node.SetVal(v)
		c.increaseFreq(node)
		return
	}
	if len(c.nodes) == c.maxCapacity {
		list := c.freqList[c.minFreq]
		delete(c.nodes, list.RemoveTailAndReturnKey())
	}
	node := NewDnode(k, v, 1)
	c.nodes[k] = node
	if c.freqList[1] == nil {
		c.freqList[1] = NewDoublyLinkedList()
	}
	c.minFreq = 1
	c.freqList[1].InsertHeadByRef(node)
}

func (c *LFUCache) increaseFreq(node *Dnode) {
	freq := node.Freq()
	list := c.freqList[freq]
	list.RemoveByRef(node)

	if freq == c.minFreq && list.Empty() {
		c.minFreq++
	}
	node.FreqIncr()
	if c.freqList[node.Freq()] == nil {
		c.freqList[node.Freq()] = NewDoublyLinkedList()
	}
	c.freqList[node.Freq()].InsertHeadByRef(node)
}


type DoublyLinkedList struct {
	head *Dnode
	tail *Dnode
}

type Dnode struct {
	val  int
	key  int
	freq int
	next *Dnode
	prev *Dnode
}

func NewDnode(key, val, freq int) *Dnode {
	return &Dnode{val: val, key: key, freq: freq}
}

func (d *Dnode) Val() int {
	return d.val
}

func (d *Dnode) SetVal(v int) {
	d.val = v
}

func (d *Dnode) Key() int {
	return d.key
}

func (d *Dnode) Freq() int {
	return d.freq
}

func (d *Dnode) FreqIncr() {
	d.freq++
}

func NewDoublyLinkedList() *DoublyLinkedList {
	return &DoublyLinkedList{}
}

func (d *DoublyLinkedList) InsertHeadByRef(node *Dnode) {
	if d.head != nil {
		d.head.prev, node.next = node, d.head
	} else {
		d.tail = node
	}
	d.head = node
}

func (d *DoublyLinkedList) Empty() bool {
	return d.head == nil
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
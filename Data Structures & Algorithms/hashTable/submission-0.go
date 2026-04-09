type HashTable struct {
	values []*linkedList
	size   int
}

func NewHashTable(capacity int) HashTable {
	values := make([]*linkedList, capacity)
	for i := range capacity {
		values[i] = newLinkedList()
	}
	return HashTable{
		values: values,
		size:   0,
	}
}

func (m *HashTable) Insert(key int, value int) {
	index := m.hash(key, len(m.values))
	m.values[index].insert(key, value)
	m.size++
	if m.size >= (len(m.values) / 2) {
		m.Resize()
	}
}

func (m *HashTable) Resize() {
	len := len(m.values)
	newLen := len * 2
	nValues := make([]*linkedList, newLen)
	for i := 0; i < newLen; i++ {
		if nValues[i] == nil {
			nValues[i] = newLinkedList()
		}
		if i >= len {
			continue
		}
		curr := m.values[i].head
		for curr != nil {
			index := m.hash(curr.key, newLen)
			if nValues[index] == nil {
				nValues[index] = newLinkedList()
			}
			nValues[index].insert(curr.key, curr.val)
			curr = curr.next
		}
	}
	m.values = nValues
}

func (m *HashTable) GetSize() int {
    return m.size
}

func (m *HashTable) GetCapacity() int {
    return  cap(m.values)
}

func (m *HashTable) Get(key int) int {
	index := m.hash(key, len(m.values))
	return m.values[index].find(key)
}

func (m *HashTable) Remove(key int) bool {
	index := m.hash(key, len(m.values))
	removed := m.values[index].remove(key)
    if removed {
        m.size--
    }
    return removed
}

func (m *HashTable) hash(key int, len int) int {
	return key % len
}

type linkedList struct {
	head *node
}

type node struct {
	val  int
	key  int
	next *node
}

func newLinkedList() *linkedList {
	return &linkedList{}
}

func (ll *linkedList) insert(key, val int) {
	curr := ll.head
	for curr != nil {
		if curr.key == key {
			curr.val = val
			break
		}
		curr = curr.next
	}
	if curr == nil {
		// not found
		ll.head = &node{val: val, key: key, next: ll.head}
	}
}

func (ll *linkedList) find(key int) int {
	val := -1
	curr := ll.head
	for curr != nil {
		if curr.key == key {
			val = curr.val
			break
		}
		curr = curr.next
	}
	return val
}

func (ll *linkedList) remove(key int) bool {
	if ll.head == nil {
		return false
	}
	curr := ll.head
	var prev *node
	for curr != nil {
		if curr.key == key {
			break
		}
		prev = curr
		curr = curr.next
	}
	if curr == nil {
		// not found
		return false
	}
	if prev == nil {
		// found (head)
		ll.head = curr.next
	} else {
		// in the middle
		prev.next = curr.next
	}
	return true
}
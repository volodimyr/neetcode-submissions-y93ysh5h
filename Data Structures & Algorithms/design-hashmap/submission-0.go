type MyHashMap struct {
	values []*linkedList
	cap    int
	size   int
}

func Constructor() MyHashMap {
	values := make([]*linkedList, 11)
	for i := range 11 {
		values[i] = newLinkedList()
	}
	return MyHashMap{
		values: values,
		size:   0,
		cap:    11,
	}
}

func (m *MyHashMap) Put(key int, value int) {
	index := m.hash(key)
	if m.values[index].insert(key, value) {
		m.size++
	}
	if m.shouldResize() {
		m.resize()
	}
}

func (m *MyHashMap) shouldResize() bool {
	return float64(m.size)/float64(m.cap) >= 0.75
}

func (m *MyHashMap) resize() {
	oldValues := m.values
	nValues := make([]*linkedList, findNextPrime(m.cap*2))
	for i := range nValues {
		nValues[i] = newLinkedList()
	}

	m.cap = len(nValues)
	m.size = 0
	m.values = nValues

	for i := 0; i < len(oldValues); i++ {
		curr := oldValues[i].head
		for curr != nil {
			index := m.hash(curr.key)
			nValues[index].insertHead(curr.key, curr.val)
			m.size++
			curr = curr.next
		}
	}
}

func (m *MyHashMap) Get(key int) int {
	index := m.hash(key)
	return m.values[index].find(key)
}

func (m *MyHashMap) Remove(key int) {
	index := m.hash(key)
	if m.values[index].remove(key) {
		m.size--
	}
}

func (m *MyHashMap) String() string {
	var s string
	for i, v := range m.values {
		s += fmt.Sprintf("[%d] = %s\n", i, v)
	}
	return s
}

func (m *MyHashMap) hash(key int) int {
	return key % m.cap
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

func (ll *linkedList) String() string {
	var s string
	curr := ll.head
	for curr != nil {
		if s == "" {
			s = fmt.Sprintf("[key = %d value = %d]", curr.key, curr.val)
		} else {
			s += fmt.Sprintf("->[key = %d value = %d]", curr.key, curr.val)
		}
		curr = curr.next
	}
	return s
}

func (ll *linkedList) insertHead(key, val int) {
	ll.head = &node{val: val, key: key, next: ll.head}
}

func (ll *linkedList) insert(key, val int) bool {
	var inserted bool
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
		inserted = true
		ll.head = &node{val: val, key: key, next: ll.head}
	}
	return inserted
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

func isPrime(num int) bool {
	if num <= 1 {
		return false
	}
	if num <= 3 {
		return true
	}
	if num%2 == 0 || num%3 == 0 {
		return false
	}
	for i := 5; int(math.Sqrt(float64(num))) >= i; i = i + 6 {
		if num%i == 0 || num%(i+2) == 0 {
			return false
		}
	}
	return true
}

func findNextPrime(n int) int {
	for {
		if isPrime(n) {
			return n
		}
		n++
	}
}


/**
 * Your MyHashMap object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Put(key,value);
 * param_2 := obj.Get(key);
 * obj.Remove(key);
 */
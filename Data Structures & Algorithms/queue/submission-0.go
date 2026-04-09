type Deque struct {
	head *deqnode
	tail *deqnode
}

type deqnode struct {
	val  int
	next *deqnode
	prev *deqnode
}

func NewDeque() *Deque {
	return &Deque{}
}

func (d *Deque) IsEmpty() bool {
	return d.head == nil
}

func (d *Deque) Append(value int) {
	n := &deqnode{val: value, prev: d.tail}
	if d.tail != nil {
		d.tail.next = n
	} else {
		d.head = n
	}
	d.tail = n
}

func (d *Deque) AppendLeft(value int) {
	n := &deqnode{val: value, next: d.head}
	if d.head != nil {
		d.head.prev = n
	} else {
		d.tail = n
	}
	d.head = n
}

func (d *Deque) Pop() int {
	if d.IsEmpty() {
		return -1
	}
	if d.head == d.tail {
		v := d.head.val
		d.head = nil
		d.tail = nil
		return v
	}
	v := d.tail.val
	d.tail = d.tail.prev
	d.tail.next = nil
	return v
}

func (d *Deque) PopLeft() int {
	if d.IsEmpty() {
		return -1
	}
	if d.head == d.tail {
		v := d.head.val
		d.head = nil
		d.tail = nil
		return v
	}
	v := d.head.val
	d.head = d.head.next
	d.head.prev = nil
	return v
}

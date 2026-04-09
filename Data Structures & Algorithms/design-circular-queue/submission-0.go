type MyCircularQueue struct {
	arr         []int
	front, rear int
	max         int
	cap         int
}

func Constructor(k int) MyCircularQueue {
	arr := make([]int, 0, k)
	for range k {
		arr = append(arr, -1)
	}
	return MyCircularQueue{
		arr:   arr,
		front: -1,
		rear:  -1,
		cap:   0,
		max:   k,
	}
}

func (m *MyCircularQueue) EnQueue(value int) bool {
	if m.IsFull() {
		return false
	}
	if m.IsEmpty() {
		m.front++
		m.rear++
		m.arr[m.rear] = value
	} else {
		if (m.rear + 1) == m.max {
			// wrap around
			m.rear = 0
		} else {
			m.rear++
		}
		m.arr[m.rear] = value
	}
	m.cap++
	return true
}

func (m *MyCircularQueue) DeQueue() bool {
	if m.IsEmpty() {
		return false
	}
	m.arr[m.front] = -1
	m.cap--
	if m.IsEmpty() {
		m.front = -1
		m.rear = -1
	} else {
		m.front++
		if m.front == m.max {
			// wrap around
			m.front = 0
		}
	}
	return true
}

func (m *MyCircularQueue) Front() int {
	if m.front == -1 {
		return -1
	}
	return m.arr[m.front]
}

func (m *MyCircularQueue) Rear() int {
	if m.rear == -1 {
		return -1
	}
	return m.arr[m.rear]
}

func (m *MyCircularQueue) IsEmpty() bool {
	return m.cap == 0
}

func (m *MyCircularQueue) IsFull() bool {
	return m.cap == m.max
}

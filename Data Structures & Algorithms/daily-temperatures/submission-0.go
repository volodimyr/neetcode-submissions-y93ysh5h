func dailyTemperatures(temperatures []int) []int {
	stack := newmstack()
	warmer := make([]int, len(temperatures))
	for i := len(temperatures) - 1; i >= 0; i-- {
		for !stack.empty() && temperatures[stack.peek()] <= temperatures[i] {
			stack.pop()
		}
		if stack.empty() {
			warmer[i] = 0
		} else {
			warmer[i] = stack.peek() - i
		}
		stack.push(i)
	}

	return warmer
}

type monotonicStack struct {
	arr []int
}

func newmstack() *monotonicStack {
	return &monotonicStack{}
}

func (m *monotonicStack) size() int {
	return len(m.arr)
}

func (m *monotonicStack) peek() int {
	if m.empty() {
		return -1
	}
	return m.arr[len(m.arr)-1]
}

func (m *monotonicStack) pop() int {
	if m.empty() {
		return -1
	}
	x := m.arr[len(m.arr)-1]
	m.arr = m.arr[:len(m.arr)-1]
	return x
}

func (m *monotonicStack) push(x int) {
	m.arr = append(m.arr, x)
}

func (m *monotonicStack) empty() bool {
	return len(m.arr) == 0
}

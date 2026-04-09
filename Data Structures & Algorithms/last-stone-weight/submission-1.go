func lastStoneWeight(stones []int) int {
	heap := newMaxHeap(stones)

	for len(heap.stones) >= 2 {
		biggest1, biggest2 := heap.pop(), heap.pop()
		if biggest1 == biggest2 {
			continue
		}
		heap.push(biggest1 - biggest2)
	}
	if len(heap.stones) == 0 {
		return 0
	}
	return heap.stones[0]
}

type maxheap struct {
	stones []int
}

func newMaxHeap(stones []int) *maxheap {
	heap := &maxheap{stones: stones}
	i := (len(heap.stones) - 1) / 2
	for i >= 0 {
		heap.percolate(i)
		i--
	}
	return heap
}

func (m *maxheap) push(stone int) {
	m.stones = append(m.stones, stone)
	i := len(m.stones) - 1
	for i > 0 && m.stones[i] > m.stones[(i-1)/2] {
		m.stones[i], m.stones[(i-1)/2] = m.stones[(i-1)/2], m.stones[i]
		i = (i - 1) / 2
	}
}

func (m *maxheap) pop() int {
	if len(m.stones) == 0 {
		return -1
	}
	if len(m.stones) == 1 {
		v := m.stones[0]
		m.stones = []int{}
		return v
	}
	v := m.stones[0]
	m.stones[0] = m.stones[len(m.stones)-1]
	m.stones = m.stones[:len(m.stones)-1]
	m.percolate(0)
	return v
}

func (m *maxheap) percolate(i int) {
	for {
		largest := i
		left := 2*i + 1
		right := 2*i + 2
		if left < len(m.stones) && m.stones[left] > m.stones[largest] {
			largest = left
		}
		if right < len(m.stones) && m.stones[right] > m.stones[largest] {
			largest = right
		}

		if largest != i {
			m.stones[largest], m.stones[i] = m.stones[i], m.stones[largest]
			i = largest
		} else {
			break
		}
	}
}

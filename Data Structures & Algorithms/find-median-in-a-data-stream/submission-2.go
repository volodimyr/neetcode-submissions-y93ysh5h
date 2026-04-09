
type MedianFinder struct {
	finder *medianHeap
}

func Constructor() MedianFinder {
	return MedianFinder{
		finder: &medianHeap{
			largest:  minheap{},
			smallest: maxheap{},
		},
	}
}

func (m *MedianFinder) AddNum(num int) {
	m.finder.Add(num)
}

func (m *MedianFinder) FindMedian() float64 {
	return m.finder.Median()
}

type medianHeap struct {
	smallest maxheap
	largest  minheap
}

func (m *medianHeap) Len() int {
	return m.smallest.Len() + m.largest.Len()
}

func (m *medianHeap) Median() float64 {
	if m.Len() == 0 {
		return 0
	}
	if m.smallest.Len() > m.largest.Len() {
		return float64(m.smallest[0])
	}
	if m.largest.Len() > m.smallest.Len() {
		return float64(m.largest[0])
	}
	min, max := float64(m.largest[0]), float64(m.smallest[0])
	return (min + max) / 2
}

func (m *medianHeap) Add(num int) {
    if m.smallest.Len() == 0 || num <= m.smallest[0] {
        heap.Push(&m.smallest, num)
    } else {
        heap.Push(&m.largest, num)
    }
    if m.smallest.Len() > m.largest.Len() + 1 {
        heap.Push(&m.largest, heap.Pop(&m.smallest).(int))
    } else if m.largest.Len() > m.smallest.Len() {
        heap.Push(&m.smallest, heap.Pop(&m.largest).(int))
    }
}

type (
	maxheap []int
	minheap []int
)

func (m maxheap) Len() int {
	return len(m)
}

func (m maxheap) Swap(i, j int) {
	m[i], m[j] = m[j], m[i]
}

func (m maxheap) Less(i, j int) bool {
	return m[i] > m[j]
}

func (m *maxheap) Push(v interface{}) {
	*m = append(*m, v.(int))
}

func (m *maxheap) Pop() interface{} {
	old := *m
	x := old[len(old)-1]
	*m = old[:len(old)-1]
	return x
}

func (m minheap) Len() int {
	return len(m)
}

func (m minheap) Swap(i, j int) {
	m[i], m[j] = m[j], m[i]
}

func (m minheap) Less(i, j int) bool {
	return m[i] < m[j]
}

func (m *minheap) Push(v interface{}) {
	*m = append(*m, v.(int))
}

func (m *minheap) Pop() interface{} {
	old := *m
	x := old[len(old)-1]
	*m = old[:len(old)-1]
	return x
}

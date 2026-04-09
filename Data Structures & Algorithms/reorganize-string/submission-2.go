func reorganizeString(s string) string {
	m := map[byte]int{}
	for i := range s {
		m[s[i]]++
	}
	maxheap := maxheap{}
	for k, v := range m {
		heap.Push(&maxheap, symbol{times: v, b: k})
	}

	var res []byte
	var prev *symbol
	for maxheap.Len() > 0 {
		pop := heap.Pop(&maxheap).(symbol)
		res = append(res, pop.b)
		pop.times--
		if prev != nil && prev.times > 0 {
			heap.Push(&maxheap, *prev)
		}
		if pop.times > 0 {
			prev = &pop
		} else {
			prev = nil
		}
	}
	if len(res) != len(s) {
		return ""
	}

	return string(res)
}

type symbol struct {
	times int
	b     byte
}

type maxheap []symbol

func (m maxheap) Len() int {
	return len(m)
}

func (m maxheap) Swap(i, j int) {
	m[i], m[j] = m[j], m[i]
}

func (m maxheap) Less(i, j int) bool {
	return m[i].times > m[j].times
}

func (m *maxheap) Push(v interface{}) {
	*m = append(*m, v.(symbol))
}

func (m *maxheap) Pop() interface{} {
	old := *m
	x := old[len(old)-1]
	*m = old[:len(old)-1]
	return x
}

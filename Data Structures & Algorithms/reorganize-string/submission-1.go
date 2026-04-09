func reorganizeString(s string) string {
	m := map[byte]int{}
	for i := range s {
		m[s[i]]++
	}
	_heap := maxheap{}
	for k, v := range m {
		heap.Push(&_heap, symbol{times: v, b: k})
	}

	var res string
	for {
		var added []symbol
		for _heap.Len() > 0 && len(added) < 2 {
			sym := heap.Pop(&_heap).(symbol)
			sym.times--
			if len(res) != 0 && res[len(res)-1] == sym.b {
				return ""
			}
			res += string(sym.b)
			added = append(added, sym)
		}
		for _, sym := range added {
			if sym.times > 0 {
				heap.Push(&_heap, sym)
			}
		}
		if _heap.Len() < 1 {
			break
		}
	}

	return res
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

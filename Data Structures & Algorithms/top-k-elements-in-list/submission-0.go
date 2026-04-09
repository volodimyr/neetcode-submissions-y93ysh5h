
func topKFrequent(nums []int, k int) []int {
	m := map[int]int{}

	for _, num := range nums {
		m[num]++
	}

	var sorted Sorted
	for k, v := range m {
		sorted = append(sorted, Counter{Val: k, Count: v})
	}
	sort.Sort(sorted)

	return sorted.TopK(k)
}

type Counter struct {
	Val   int
	Count int
}

type Sorted []Counter

func (s Sorted) TopK(k int) []int {
	var arr []int
	for i := 0; i < k; i++ {
		arr = append(arr, s[i].Val)
	}
	return arr
}
func (s Sorted) Len() int           { return len(s) }
func (s Sorted) Swap(i, j int)      { s[i], s[j] = s[j], s[i] }
func (s Sorted) Less(i, j int) bool { return s[i].Count > s[j].Count }
// Definition for a pair.
// type Pair struct {
//     Key   int
//     Value string
// }

type Solution struct {

}

func NewSolution() *Solution {
return &Solution{}
}

func QuickSort(pairs []Pair) []Pair {
	quick(pairs, 0, len(pairs)-1)
	return pairs
}

func quick(pairs []Pair, s, e int) {
	if e-s+1 <= 1 {
		return
	}

	left := s
	pivot := pairs[e]
	for i := s; i < e; i++ {
		if pairs[i].Key < pivot.Key {
			pairs[left], pairs[i] = pairs[i], pairs[left]
			left++
		}
	}
	pairs[e], pairs[left] = pairs[left], pivot
	quick(pairs, s, left-1)
	quick(pairs, left+1, e)
}
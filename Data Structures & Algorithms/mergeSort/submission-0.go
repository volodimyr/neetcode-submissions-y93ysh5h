// Definition for a pair.
// type Pair struct {
//     Key   int
//     Value string
// }

func mergeSort(pairs []Pair) []Pair {
	sort1(pairs, 0, len(pairs)-1)
	return pairs
}

func sort1(pairs []Pair, l, r int) {
	if l < r {
		m := (l + r) / 2
		sort1(pairs, l, m)
		sort1(pairs, m+1, r)

		merge(pairs, l, m, r)
	}
}

func merge(pairs []Pair, l, m, r int) {
	L := make([]Pair, m-l+1)
	R := make([]Pair, r-m)
	copy(L, pairs[l:m+1])
	copy(R, pairs[m+1:r+1])

	var i, j int
	k := l

	for i < len(L) && j < len(R) {
		if L[i].Key <= R[j].Key {
			pairs[k] = L[i]
			i++
		} else {
			pairs[k] = R[j]
			j++
		}
		k++
	}

	for i < len(L) {
		pairs[k] = L[i]
		i++
		k++
	}
	for j < len(R) {
		pairs[k] = R[j]
		j++
		k++
	}
}
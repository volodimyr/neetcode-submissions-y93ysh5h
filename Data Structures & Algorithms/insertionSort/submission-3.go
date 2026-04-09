func insertionSort(pairs []Pair) [][]Pair {
	n := len(pairs)
	if n == 0 {
		return [][]Pair{}
	}

	sorted := make([][]Pair, 0, n)
	state := make([]Pair, n)
	copy(state, pairs)
	sorted = append(sorted, state)

	if n == 1 {
		return sorted
	}

	for i := 1; i < n; i++ {
		key := pairs[i]
		j := i - 1

		for j >= 0 && pairs[j].Key > key.Key {
			pairs[j+1] = pairs[j]
			j--
		}
		pairs[j+1] = key

		state := make([]Pair, n)
		copy(state, pairs)
		sorted = append(sorted, state)
	}

	return sorted
}

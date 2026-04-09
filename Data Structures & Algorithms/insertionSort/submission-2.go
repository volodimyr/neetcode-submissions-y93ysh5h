func insertionSort(pairs []Pair) [][]Pair {
    	if len(pairs) == 0 {
		return [][]Pair{}
	}
	state := make([]Pair, len(pairs))
	copy(state, pairs)
	sorted := [][]Pair{state}
	if len(pairs) <= 1 {
		return sorted
	}

	for i := 1; i < len(pairs); i++ {
		for j := i - 1; j >= 0 && pairs[j].Key > pairs[j+1].Key; j-- {
			pairs[j], pairs[j+1] = pairs[j+1], pairs[j]
		}
		// save state
		state := make([]Pair, len(pairs))
		copy(state, pairs)
		sorted = append(sorted, state)

	}
	return sorted
}
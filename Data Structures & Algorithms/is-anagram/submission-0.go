func isAnagram(s string, t string) bool {
	m := map[rune]int{}
	for _, r := range s {
		found, ok := m[r]
		if ok {
			m[r] = found + 1
		} else {
			m[r] = 1
		}
	}
	for _, r := range t {
		found, ok := m[r]
		if !ok {
			return false
		}
		found = found - 1
		if found == 0 {
			delete(m, r)
		} else {
			m[r] = found
		}
	}

	return len(m) == 0
}

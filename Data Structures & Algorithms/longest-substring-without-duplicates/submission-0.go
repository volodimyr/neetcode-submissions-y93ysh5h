func lengthOfLongestSubstring(s string) int {
	m := map[byte]int{}
	var _max int
	var start int
	for i := 0; i < len(s); i++ {
		j, ok := m[s[i]]
		if ok {
			for start <= j {
				delete(m, s[start])
				start++
			}
		}
		m[s[i]] = i

		_max = max(_max, len(m))
	}
	return _max
}
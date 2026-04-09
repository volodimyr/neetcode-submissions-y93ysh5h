
func mergeAlternately(word1 string, word2 string) string {
		n, m := len(word1), len(word2)
	var b bytes.Buffer
	b.Grow(n + m)

	maxLen := max(n, m)
	for i := 0; i < maxLen; i++ {
		if i < n {
			b.WriteByte(word1[i])
		}
		if i < m {
			b.WriteByte(word2[i])
		}

	}

	return b.String()
}

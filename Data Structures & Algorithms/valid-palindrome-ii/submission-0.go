func validPalindrome(s string) bool {
	return valid(s, false)
}

func valid(str string, skipped bool) bool {
	s, e := 0, len(str)-1
	for s < e {
		if str[s] != str[e] {
			if skipped {
				return false
			}
			return valid(str[s+1:e+1], true) || valid(str[s:e], true)
		}
		s++
		e--
	}

	return true
}
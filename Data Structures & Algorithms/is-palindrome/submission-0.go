func isPalindrome(s string) bool {
	i := 0
	j := len(s) - 1
	for i < j {
		chi := s[i]
		if !alphanumeric(chi) {
			i++
			continue
		}
		chj := s[j]
		if !alphanumeric(chj) {
			j--
			continue
		}
		if !equal(chi, chj) {
			return false
		}
		i++
		j--
	}
	return true
}

func equal(a, b byte) bool {
	if a <= '9' && a >= '0' {
		return a == b
	}
	return toLower(a) == toLower(b)
}

func toLower(b byte) byte {
	if b >= 'A' && b <= 'Z' {
		return b + 32
	}
	return b
}

func alphanumeric(c byte) bool {
	return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') || (c >= '0' && c <= '9')
}

func longestCommonPrefix(strs []string) string {
	if len(strs) == 1 {
		return strs[0]
	}
	prefix := len(strs[0])
	for _, str := range strs[1:] {
		var tempPref int
		for i, s := range strs[0][:prefix] {
			if i >= len(str) {
				break
			}
			if byte(s) == str[i] {
				tempPref++
			} else {
				break
			}
		}
		if tempPref == 0 {
			return ""
		}
		if prefix > tempPref {
			prefix = tempPref
		}
	}

	return strs[0][:prefix]
}
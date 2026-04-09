func groupAnagrams(strs []string) [][]string {
	m := map[[26]int][]string{}
	for _, str := range strs {
		arr := [26]int{}
		for _, s := range str {
			arr[s-'a'] += 1
		}
		m[arr] = append(m[arr], str)
	}
	res := make([][]string, len(m))
	var index int
	for _, arr := range m {
		res[index] = arr
		index++
	}
	return res
}
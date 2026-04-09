func twoSum(numbers []int, target int) []int {
	for i, number := range numbers {
		t := target - number
		found := search(numbers, i, t, 0, len(numbers)-1)
		if found == -1 {
			continue
		}
		if i < found {
			return []int{i + 1, found + 1}
		}
		return []int{found + 1, i + 1}
	}
	return []int{}
}

func search(numbers []int, index, t, s, e int) int {
    for s <= e {
        m := s + (e-s)/2
        if numbers[m] == t && index != m {
            return m
        }
        if numbers[m] < t {
            s = m + 1
        } else {
            e = m - 1
        }
    }
    return -1
}
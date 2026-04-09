func sortColors(nums []int) {
	arr := [3]int{}
	for _, n := range nums {
		arr[n] += 1
	}

	var index int
	for color, times := range arr {
		for range times {
			nums[index] = color
			index++
		}
	}
}

func sortArray(nums []int) []int {
	sort1(nums, 0, len(nums)-1)
	return nums
}

func sort1(nums []int, s, e int) {
	if e-s+1 <= 1 {
		return
	}

	pivot := nums[e]
	left := s

	for i := s; i < e; i++ {
		if nums[i] <= pivot {
			nums[left], nums[i] = nums[i], nums[left]
			left++
		}
	}
	nums[e] = nums[left]
	nums[left] = pivot

	sort1(nums, s, left-1)
	sort1(nums, left+1, e)
}
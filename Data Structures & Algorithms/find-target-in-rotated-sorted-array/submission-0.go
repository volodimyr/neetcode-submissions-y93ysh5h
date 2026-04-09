func search(nums []int, target int) int {
	L, R := 0, len(nums)-1
	for L <= R {
		m := (L + R) / 2
		if target == nums[m] {
			return m
		}
		if nums[L] <= nums[m] {
			if target < nums[m] && target >= nums[L] {
				//sorted
				R = m - 1
			} else {
				L = m + 1
			}
		} else {
			if target > nums[m] && target <= nums[R] {
				//sorted
				L = m + 1
			} else {
				R = m - 1
			}
		}
	}
	return -1
}

func productExceptSelf(nums []int) []int {
	res := make([]int, len(nums))

	prefix := 1
	for i := range nums {
		prefix *= nums[i]
		res[i] = prefix
	}
	suffix := 1
	for i := len(nums) - 1; i >= 0; i-- {
		p := 1
		if (i - 1) >= 0 {
			p = res[i-1]
		}
		res[i] = p * suffix
		suffix *= nums[i]
	}

	return res
}

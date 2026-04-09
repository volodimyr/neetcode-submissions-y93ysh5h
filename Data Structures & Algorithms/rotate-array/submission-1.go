func rotate(nums []int, k int) {
	k = k % len(nums)
	if k == 0 {
		return
	}
	k = k % len(nums)
	if k == 0 {
		return
	}
	reverse(nums)
	reverse(nums[:k])
	reverse(nums[k:])
	fmt.Println(nums)
}

func reverse(nums []int) {
	for i, j := 0, len(nums)-1; i < j; {
		nums[i], nums[j] = nums[j], nums[i]
		i++
		j--
	}
}

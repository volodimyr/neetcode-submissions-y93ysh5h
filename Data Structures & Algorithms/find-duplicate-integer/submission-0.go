func findDuplicate(nums []int) int {
	slow, fast := nums[0], nums[0]
	for {
		slow = nums[slow]
		fast = nums[nums[fast]]
		if fast == slow {
			break
		}
	}
	slow2 := nums[0]
	for slow2 != slow {
		slow = nums[slow]
		slow2 = nums[slow2]
	}
	return slow
}
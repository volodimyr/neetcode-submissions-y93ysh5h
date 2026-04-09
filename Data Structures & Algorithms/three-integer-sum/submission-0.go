func threeSum(nums []int) [][]int {
	sort.Ints(nums)
	res := [][]int{}

	for i := range len(nums) - 2 {
		if i > 0 && nums[i-1] == nums[i] {
			continue
		}

		L := i + 1
		R := len(nums) - 1

		for L < R {
			total := nums[i] + nums[L] + nums[R]
			if total == 0 {
				res = append(res, []int{nums[i], nums[L], nums[R]})

				for L < R && nums[R] == nums[R-1] {
					R--
				}

				for L < R && nums[L] == nums[L+1] {
					L++
				}

				R--
				L++
			} else if total > 0 {
				R--
			} else {
				L++
			}
		}
	}
	return res
}

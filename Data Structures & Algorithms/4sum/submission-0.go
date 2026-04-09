func fourSum(nums []int, target int) [][]int {
	sort.Ints(nums)
	res := [][]int{}

	for i := range len(nums) - 3 {
		if i > 0 && nums[i-1] == nums[i] {
			continue
		}
		for L := i + 1; L < len(nums)-2; L++ {
			if L > i+1 && nums[L] == nums[L-1] {
				continue
			}
			L1 := L + 1
			R := len(nums) - 1
		    for L1 < R {
                total := nums[i] + nums[L] + nums[L1] + nums[R]
                if total == target {
                    res = append(res, []int{nums[i], nums[L], nums[L1], nums[R]})
					for L1 < R && nums[L1] == nums[L1+1] {
						L1++
					}
					for L1 < R && nums[R] == nums[R-1] {
						R--
					}
					L1++
					R--
			    } else if total > target {
				    R--
			    } else {
				    L1++
			    }
		    }
        }
	}
	return res
}

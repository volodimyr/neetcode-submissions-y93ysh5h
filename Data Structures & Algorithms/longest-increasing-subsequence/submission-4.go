func lengthOfLIS(nums []int) int {
	dp := []int{}
	dp = append(dp, nums[0])

	LIS := 1
	for i := 1; i < len(nums); i++ {
		if dp[len(dp)-1] < nums[i] {
			dp = append(dp, nums[i])
			LIS++
			continue
		}

		idx := sort.Search(len(dp), func(j int) bool {
			return dp[j] >= nums[i]
		})
		dp[idx] = nums[i]
	}

	return LIS
}
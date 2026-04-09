func maxSubArray(nums []int) int {
    _max := nums[0]
    cur := 0
    for _, n := range nums {
        cur = max(cur, 0)
        cur += n
        _max = max(_max, cur)
    }
    return _max
}

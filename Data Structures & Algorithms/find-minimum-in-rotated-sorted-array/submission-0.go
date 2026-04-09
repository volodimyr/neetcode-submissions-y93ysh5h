func findMin(nums []int) int {
    if len(nums) == 1 {
        return nums[0]
    }
    L, R := 0, len(nums)-1 
    var min int
    if nums[0] > nums[len(nums)-1] {
        min = nums[len(nums)-1]
    }else {
       min = nums[0]
    }
    for L <= R {
        mid := (L+R) / 2

        nMin := nums[mid]
        if nMin >= min {
            L = mid + 1
        }else {
            min = nMin
            R = mid -1
        }
    }
    return min
}

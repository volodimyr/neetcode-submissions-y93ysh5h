func search(nums []int, target int) int {
    low, high := 0, len(nums)-1
    for low <= high {
        mid := low +(high-low)/2
        v := nums[mid]
        if v == target {
            return mid
        }
        if v < target {
            low = mid +1
        }else {
            high = mid -1
        }
    }
    return -1
}

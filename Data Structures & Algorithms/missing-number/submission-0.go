func missingNumber(nums []int) int {
    var sum int
    for i := range len(nums)+1 {
        sum+=i
    }
    var actual int
    for _, num := range nums {
        actual+=num
    }
    return sum-actual
}
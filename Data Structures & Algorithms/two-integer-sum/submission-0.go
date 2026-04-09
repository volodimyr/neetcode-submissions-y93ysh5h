func twoSum(nums []int, target int) []int {
    m := map[int][]int{}
    for i, n := range nums {
        exists, ok := m[target-n]
        if ok {
            exists = append(exists, i)
            return exists
        }
        m[n] = []int{i}
    }
    return []int{}
}

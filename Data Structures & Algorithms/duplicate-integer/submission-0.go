func hasDuplicate(nums []int) bool {
    m := map[int]struct{}{}
    for _, n := range nums{
        _, ok := m[n]
        if ok {
            return true
        }
        m[n] = struct{}{}
    }
    return false
}

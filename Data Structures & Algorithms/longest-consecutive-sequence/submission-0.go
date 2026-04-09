func longestConsecutive(nums []int) int {
    var _max int
    m := make(map[int]struct{}, 0)
    for _, n := range nums {
        m[n] = struct{}{}
        sq := 1
        for i := n-1; ; i-- {
            _, ok := m[i]
            if !ok {
                break
            }
            sq++
        }
        for i := n +1; ; i++ {
            _, ok := m[i]
            if !ok {
                break
            }
            sq++
        }
        _max = max(_max, sq)
    }
    return _max
}

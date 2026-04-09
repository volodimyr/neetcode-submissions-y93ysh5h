func longestConsecutive(nums []int) int {
    var _max int
    set := make(map[int]struct{}, 0)
    
    for _, n := range nums {
        set[n] = struct{}{}
    }
    for n := range set {
        if _, ok := set[n-1]; ok {
            continue
        }
        count := 1
        start := n+1
        for {
            _, ok := set[start]
            if !ok {
                break
            }
            start++
            count++
        }
        _max = max(_max, count)
    }

    return _max
}

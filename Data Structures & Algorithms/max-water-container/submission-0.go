func maxArea(height []int) int {
    L, R := 0, len(height)-1
    var water int
    for L < R {
        water = max(water, (R-L) * min(height[L], height[R]))
        if height[L] < height[R] {
            L++
        }else{
            R--
        }
    }
    return water
}
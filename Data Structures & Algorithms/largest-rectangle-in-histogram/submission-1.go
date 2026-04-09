func largestRectangleArea(heights []int) int {
    if len(heights)==0 {
        return 0
    }
    maxarea := heights[0]
    for i, h := range heights[:len(heights)-1] {
        base := h
        for j := i+1; j < len(heights); j++ {
            if heights[j] < base {
                base = heights[j]
            }
            maxarea = max(maxarea, (j-i+1)*base, heights[j])
        }
    }

    return maxarea
}
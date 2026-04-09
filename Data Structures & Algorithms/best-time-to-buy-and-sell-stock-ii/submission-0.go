func maxProfit(prices []int) int {
    sum := 0
    b := prices[0]
    for R :=1; R < len(prices); R++ {
        if prices[R] - b <= 0 {
            b = prices[R]
        }else {
            sum += (prices[R] - b)
            b = prices[R]
        }
    }

    return sum
}
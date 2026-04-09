func maxProfit(prices []int) int {
	var _max int
	min := prices[0]
	for R := range len(prices) {
		if min > prices[R] {
			min = prices[R]
		}
		_max = max(_max, prices[R]-min)
	}
	return _max
}
func trap(height []int) int {
	if len(height) < 2 {
		return 0
	}
	R := len(height) - 1
	L := 0
	var sum int

	maxr, maxl := R-1, L+1
	for L < R {
		if height[L] < height[R] {
			var ocuppied int
			for height[maxl] < height[L] && maxl != R {
				ocuppied += height[maxl]
				maxl++
			}
			sum += min(height[L], height[maxl]) * (maxl - L - 1)
			sum -= ocuppied
			L = maxl
			maxl++
		} else {
			var occupied int
			for height[maxr] < height[R] && maxr != L {
				occupied += height[maxr]
				maxr--
			}
			sum += min(height[R], height[maxr]) * (R - maxr - 1)
			sum -= occupied
			R = maxr
			maxr--
		}
	}
	return sum
}

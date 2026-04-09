func trap(height []int) int {
	if len(height) < 2 {
		return 0
	}
	R := len(height) - 1
	L := 0
	for R > 0 {
		if height[R-1] > height[R] {
			R--
		} else {
			break
		}
	}
	var (
		sum int
	)

	for L < len(height)-1 {
		if height[L+1] > height[L] {
			L++
		} else {
			break
		}
	}

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
			if maxl >= R-1 {
				break
			}
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
			if maxr <= L+1 {
				break
			}
			R = maxr
			maxr--
		}
	}
	return sum
}
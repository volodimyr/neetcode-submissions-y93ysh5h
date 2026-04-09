func trap(height []int) int {
	if len(height) < 2 {
		return 0
	}
	L, R := 0, 1
	maxr := len(height) - 1
	for maxr > L {
		if height[maxr-1] > height[maxr] {
			maxr--
		} else {
			break
		}
	}
	var (
		sum      int
		negative int
	)
	for R <= maxr {
		if height[L] > height[R] && R != maxr {
			negative += height[R]
		} else {
			sum += calc(height, L, R)
			negative = 0
			L = R
		}
		R++
	}
	return sum
}

func calc(height []int, i, j int) int {
	waterLevel := min(height[i], height[j])
	capacity := waterLevel * (j - i - 1)
	occupied := 0
	for k := i + 1; k < j; k++ {
		occupied += min(height[k], waterLevel)
	}
	return capacity - occupied
}

func minEatingSpeed(piles []int, h int) int {
	var R int
	for _, pile := range piles {
		if pile >= R {
			//max
			R = pile
		}
	}
	if len(piles) == h {
		return R
	}

	L := 1
	var k int

	for L <= R {
		var total int
		speed := (L + R) / 2

		for _, pile := range piles {
			total += int(math.Ceil(float64(pile) / float64(speed)))
		}
		if total <= h {
			k = speed
			R = speed - 1
		} else {
			L = speed + 1
		}
	}
	return k
}
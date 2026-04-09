type cars struct {
	ps []int
	sp []int
}

func (c *cars) Len() int {
	return len(c.ps)
}

func (c *cars) Less(i, j int) bool {
	return c.ps[i] > c.ps[j]
}

func (c *cars) Swap(i, j int) {
	c.ps[i], c.ps[j] = c.ps[j], c.ps[i]
	c.sp[i], c.sp[j] = c.sp[j], c.sp[i]
}

func carFleet(target int, position []int, speed []int) int {
	sorted := cars{ps: position, sp: speed}
	sort.Sort(&sorted)
	cars := []car{newCar(target, sorted.ps[0], sorted.sp[0])}
	for i := 1; i < len(sorted.ps); i++ {
		car := newCar(target, sorted.ps[i], sorted.sp[i])
		if cars[len(cars)-1].t < car.t {
			cars = append(cars, car)
		}
	}
	return len(cars)
}

type car struct {
	t float64
}

func newCar(target, ps, sp int) car {
	timeToTarget := float64(target-ps) / float64(sp)
	return car{t: timeToTarget}
}

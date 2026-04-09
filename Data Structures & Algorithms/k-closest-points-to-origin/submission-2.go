func kClosest(points [][]int, max int) [][]int {
	arr := [][]int{}
	for i := 0; i < len(points); i++ {
		if i < max {
			arr = append(arr, points[i])
			j := len(arr) - 1
			for j > 0 && distance(arr[(j-1)/2]) < distance(arr[j]) {
				arr[(j-1)/2], arr[j] = arr[j], arr[(j-1)/2]
				j = (j - 1) / 2
			}

		} else if distance(points[i]) < distance(arr[0]) {
			arr[0] = points[i]
			j := 0
			for {
				largest := j
				left := 2*j + 1
				right := 2*j + 2

				if left < len(arr) && distance(arr[left]) > distance(arr[largest]) {
					largest = left
				}
				if right < len(arr) && distance(arr[right]) > distance(arr[largest]) {
					largest = right
				}
				if largest != j {
					arr[j], arr[largest] = arr[largest], arr[j]
					j = largest
				} else {
					break
				}
			}
		}
	}

	return arr
}

func distance(points []int) int {
	return points[0]*points[0] + points[1]*points[1]
}
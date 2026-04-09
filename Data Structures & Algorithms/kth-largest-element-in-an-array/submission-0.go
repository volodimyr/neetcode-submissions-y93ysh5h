func findKthLargest(nums []int, max int) int {
	arr := []int{}
	for i, n := range nums {
		if i < max {
			arr = append(arr, n)
			j := len(arr) - 1
			for j > 0 && arr[j] < arr[(j-1)/2] {
				arr[j], arr[(j-1)/2] = arr[(j-1)/2], arr[j]
				j = (j - 1) / 2
			}
		} else if n > arr[0] {
			arr[0] = n
			j := 0
			for 2*j+1 < len(arr) {
				if 2*j+2 < len(arr) && arr[2*j+2] < arr[2*j+1] && arr[j] > arr[2*j+2] {
					arr[j], arr[2*j+2] = arr[2*j+2], arr[j]
					j = 2*j + 2
				} else if arr[j] > arr[2*j+1] {
					arr[j], arr[2*j+1] = arr[2*j+1], arr[j]
					j = 2*j + 1
				} else {
					break
				}
			}
		}
	}
	return arr[0]
}

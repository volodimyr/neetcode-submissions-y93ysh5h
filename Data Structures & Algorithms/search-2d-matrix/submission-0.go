func searchMatrix(matrix [][]int, target int) bool {
	rows, columns := len(matrix), len(matrix[0])

	low, high := 0, rows*columns-1

	for low <= high {
		mid := low + (high-low)/2
		val := matrix[mid/columns][mid%columns]
		if val == target {
			return true
		}
		if val > target {
			high = mid - 1
		} else {
			low = mid + 1
		}
	}
	return false
}
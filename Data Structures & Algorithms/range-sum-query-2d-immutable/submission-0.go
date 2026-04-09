type NumMatrix struct {
	prefix [][]int
	matrix [][]int
}

func Constructor(matrix [][]int) NumMatrix {
	prefix := make([][]int, len(matrix))
	for i := range matrix {
		prefix[i] = make([]int, len(matrix[i]))
		var sum int
		for j := range matrix[i] {
			sum += matrix[i][j]
			prefix[i][j] = sum
		}
	}
	return NumMatrix{
		matrix: matrix,
		prefix: prefix,
	}
}

func (n *NumMatrix) SumRegion(row1 int, col1 int, row2 int, col2 int) int {
	var sum int
	for row1 <= row2 {
		sum += n.sum(row1, col1, col2)
		row1++
	}

	return sum
}

func (n *NumMatrix) sum(row, left, right int) int {
	sum := n.prefix[row][right]
	if left == 0 {
		return sum
	}
	sum -= n.prefix[row][left-1]
	return sum
}

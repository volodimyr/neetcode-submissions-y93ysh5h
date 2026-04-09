
func isValidSudoku(board [][]byte) bool {
	for row := range len(board) {
		if !valid(board[row]) {
			return false
		}
	}
	for col := range len(board) {
		if !valid(extractcol(col, board)) {
			return false
		}
	}

	for i := 0; i <= len(board)-3; i += 3 {
		for j := 0; j <= len(board[i])-3; j += 3 {
			if !valid(extractbox(i, j, board)) {
				return false
			}
		}
	}

	return true
}

func extractbox(row, col int, board [][]byte) []byte {
	arr := make([]byte, 9)
	var index int
	for i := row; i < row+3; i++ {
		for j := col; j < col+3; j++ {
			arr[index] = board[i][j]
			index++
		}
	}
	return arr
}

func extractcol(col int, board [][]byte) []byte {
	arr := make([]byte, len(board))
	for i := range len(board) {
		arr[i] = board[i][col]
	}
	return arr
}

func valid(arr []byte) bool {
	counter := make([]int, 10)
	for _, a := range arr {
		if a == '.' {
			continue
		}
		id := a-'0'
		c := counter[id]
		if c > 0 {
			return false
		}
		counter[id]++
	}
	return true
}
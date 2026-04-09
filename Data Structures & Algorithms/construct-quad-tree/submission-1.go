
func construct(grid [][]int) *Node {
    return build(grid, 0, 0, len(grid))
}

func build(grid [][]int, i, j, size int) *Node{
    if samenumb(grid, i, j, size) {
        return &Node{
            IsLeaf: true,
            Val: grid[i][j] == 1,
        }
    }
    half := size / 2
    return &Node{
        IsLeaf: false,
        Val: true,
        TopLeft: build(grid, i, j, half),
        TopRight: build(grid, i, j+half, half),
        BottomLeft: build(grid, i+half, j, half),
        BottomRight: build(grid, i+half, j+half, half),
    }
}

func samenumb(grid [][]int, row, col, size int) bool {
    numb := grid[row][col]
    for i:= row; i < row+size; i++ {
        for j := col; j < col+size; j++ {
            if numb != grid[i][j] {
                return false
            }
        }
    }
    return true
}
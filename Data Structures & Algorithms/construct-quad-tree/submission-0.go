
func construct(grid [][]int) *Node {
    if samenumb(grid) {
        return &Node{
            IsLeaf: true,
            Val: grid[0][0] != 0,
        }
    }

    node := &Node{
        IsLeaf: false,
        Val: true,
    }

    rows := len(grid)
    cols := len(grid[0])
    midRow := rows / 2
    midCol := cols / 2

    tl := [][]int{}
    tr := [][]int{}
    bl := [][]int{}
    br := [][]int{}
    for i := 0; i < midRow; i++ {
        tl = append(tl, grid[i][:midCol])
    }
    for i := 0; i < midRow; i++ {
        tr = append(tr, grid[i][midCol:])
    }
    for i := midRow; i < rows; i++ {
        bl = append(bl, grid[i][:midCol])
    }
    for i := midRow; i < rows; i++ {
        br = append(br, grid[i][midCol:])
    }
    node.TopLeft = construct(tl)
    node.TopRight = construct(tr)
    node.BottomLeft = construct(bl)
    node.BottomRight = construct(br)

    return node
}

func samenumb(grid [][]int) bool {
    numb := grid[0][0]
    for i:=0;i< len(grid);i++ {
        for j :=0; j < len(grid[i]); j++ {
            if numb != grid[i][j] {
                return false
            }
        }
    }
    return true
}
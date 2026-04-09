type Codec struct {
}

func Constructor() Codec {
	return Codec{}
}

func (c *Codec) serialize(root *TreeNode) string {
	var b strings.Builder
	q := []*TreeNode{}
	q = append(q, root)

	for len(q) != 0 {
		node := q[0]
		q = q[1:]
		if b.Len() > 0 {
			b.WriteString(",")
		}
		if node != nil {
			b.WriteString(strconv.Itoa(node.Val))
			q = append(q, node.Left)
			q = append(q, node.Right)
		} else {
			b.WriteString("nil")
		}

	}
	return b.String()
}

func (c *Codec) deserialize(data string) *TreeNode {
	var root *TreeNode
	stream, ok := newStream(data)
	if !ok {
		return root
	}
	root = stream.next()
	if stream.empty() {
		return root
	}
	q := []*TreeNode{root}

	for len(q) != 0 {
		if stream.empty() {
			return root
		}
		node := q[0]
		q = q[1:]
		node.Left = stream.next()
		if node.Left != nil {
			q = append(q, node.Left)
		}
		if stream.empty() {
			return root
		}
		node.Right = stream.next()
		if node.Right != nil {
			q = append(q, node.Right)
		}
	}
	return root
}

type stream struct {
	arr []string
	cur int
}

func newStream(data string) (*stream, bool) {
	if len(data) == 0 {
		return nil, false
	}
	arr := strings.Split(data, ",")
	if len(arr) == 0 {
		return nil, false
	}
	return &stream{
		arr: arr,
		cur: 0,
	}, true
}

func (s *stream) empty() bool {
	return s.cur == len(s.arr)
}

func (s *stream) next() *TreeNode {
	data := s.arr[s.cur]
	s.cur++
	return s.node(data)
}

func (s *stream) node(data string) *TreeNode {
	if data == "nil" {
		return nil
	}
	v, _ := strconv.Atoi(data)
	return &TreeNode{Val: v}
}
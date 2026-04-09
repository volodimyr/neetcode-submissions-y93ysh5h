type Solution struct {
	whitespaces []int
}

func (s *Solution) Encode(strs []string) string {
	builder := strings.Builder{}
	s.whitespaces = []int{}
	for _, str := range strs {
		s.whitespaces = append(s.whitespaces, len(str))
		builder.WriteString(str)
	}
	return builder.String()
}

func (s *Solution) Decode(str string) []string {
	var curr int
	var arr []string
	for _, ws := range s.whitespaces {
		end := ws + curr
		builder := strings.Builder{}
		for ; curr < end; curr++ {
			builder.WriteByte(str[curr])
		}
		arr = append(arr, builder.String())
	}
	return arr
}

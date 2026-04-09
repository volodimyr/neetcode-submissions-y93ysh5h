func evalRPN(tokens []string) int {
	var values []int

	for _, token := range tokens {
		val, err := strconv.Atoi(token)
		if err == nil {
			values = append(values, val)
			continue
		}
		total := values[len(values)-1]
		n1 := values[len(values)-2]
		values = values[:len(values)-2]

		switch token {
		case "+":
			values = append(values, n1+total)
		case "-":
			values = append(values, n1-total)
		case "/":
			values = append(values, n1/total)
		case "*":
			values = append(values, n1*total)
		}
	}
	return values[len(values)-1]
}
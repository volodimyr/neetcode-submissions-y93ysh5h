type FreqStack struct {
	max    int
	stacks map[int][]int
	freq   map[int]int
}

func Constructor() FreqStack {
	return FreqStack{
		max:    1,
		freq:   map[int]int{},
		stacks: map[int][]int{},
	}
}

func (f *FreqStack) Push(val int) {
	fq, ok := f.freq[val]
	if !ok {
		fq = 1
	} else {
		fq++
	}
	f.freq[val] = fq
	stack, ok := f.stacks[fq]
	if !ok {
		stack = []int{val}
	} else {
		stack = append(stack, val)
	}
	f.stacks[fq] = stack
	if fq > f.max {
		f.max = fq
	}
}

func (f *FreqStack) Pop() int {
	stack := f.stacks[f.max]
	v := stack[len(stack)-1]
	f.stacks[f.max] = stack[:len(stack)-1]
	if len(f.stacks[f.max]) == 0 {
		delete(f.stacks, f.max)
		f.max--
	}
	f.freq[v]--
	return v
}
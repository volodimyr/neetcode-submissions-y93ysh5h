type value struct {
	val int
	min int
}

type MinStack struct {
	arr []value
}

func Constructor() MinStack {
	return MinStack{
		arr: make([]value, 0),
	}
}

func (this *MinStack) Push(val int) {
	if this.empty() {
		this.arr = append(this.arr, value{val: val, min: val})
		return
	}
	peeked := this.peek()
	if peeked.min < val {
		this.arr = append(this.arr, value{val: val, min: peeked.min})
	} else {
		this.arr = append(this.arr, value{val: val, min: val})
	}
}

func (this *MinStack) empty() bool {
	return len(this.arr) == 0
}

func (this *MinStack) Pop() {
	this.arr = this.arr[:len(this.arr)-1]
}

func (this *MinStack) peek() value {
	return this.arr[len(this.arr)-1]
}

func (this *MinStack) Top() int {
	return this.arr[len(this.arr)-1].val
}

func (this *MinStack) GetMin() int {
	return this.arr[len(this.arr)-1].min
}

type KthLargest struct {
	arr []int
	max int
}

func Constructor(k int, nums []int) KthLargest {
	kth := KthLargest{
		arr: []int{},
		max: k,
	}
	for _, n := range nums {
		kth.Add(n)
	}

	return kth
}

func (k *KthLargest) Add(val int) int {
	if k.max > len(k.arr) {
		k.arr = append(k.arr, val)
		k.heapifyUp()
	} else if val > k.arr[0] {
		k.arr[0] = val
		k.heapifyDown()
	}
	return k.arr[0]
}

func (k *KthLargest) heapifyUp() {
	i := len(k.arr) - 1
	for i > 0 && k.arr[i] < k.arr[(i-1)/2] {
		k.arr[i], k.arr[(i-1)/2] = k.arr[(i-1)/2], k.arr[i]
		i = (i - 1) / 2
	}
}

func (k *KthLargest) heapifyDown() {
	i := 0
	for (2*i + 1) < len(k.arr) {
		if 2*i+2 < len(k.arr) && k.arr[2*i+2] < k.arr[2*i+1] && k.arr[i] > k.arr[2*i+2] {
			k.arr[2*i+2], k.arr[i] = k.arr[i], k.arr[2*i+2]
			i = 2*i + 2
		} else if k.arr[2*i+1] < k.arr[i] {
			k.arr[2*i+1], k.arr[i] = k.arr[i], k.arr[2*i+1]
			i = 2*i + 1
		} else {
			break
		}
	}
}

type MinHeap struct {
	arr []int
}

func NewMinHeap() *MinHeap {
	return &MinHeap{
		arr: []int{0},
	}
}

func (mh *MinHeap) Push(val int) {
	mh.arr = append(mh.arr, val)
	i := len(mh.arr) - 1
	for i > 1 && mh.arr[i] < mh.arr[i/2] {
		mh.arr[i/2], mh.arr[i] = mh.arr[i], mh.arr[i/2]
		i = i / 2
	}
}

func (mh *MinHeap) Pop() int {
	if len(mh.arr) == 1 {
		return -1
	}
	if len(mh.arr) == 2 {
		v := mh.arr[len(mh.arr)-1]
		mh.arr = mh.arr[:len(mh.arr)-1]
		return v
	}

	res := mh.arr[1]
	mh.arr[1] = mh.arr[len(mh.arr)-1]
	mh.arr = mh.arr[:len(mh.arr)-1]
	i := 1
	for 2*i < len(mh.arr) {
		if 2*i+1 < len(mh.arr) && mh.arr[2*i+1] < mh.arr[2*i] && mh.arr[i] > mh.arr[2*i+1] {
			mh.arr[2*i+1], mh.arr[i] = mh.arr[i], mh.arr[2*i+1]
			i = 2*i + 1
		} else if mh.arr[2*i] < mh.arr[i] {
			mh.arr[2*i], mh.arr[i] = mh.arr[i], mh.arr[2*i]
			i = 2 * i
		} else {
			break
		}
	}

	return res
}

func (mh *MinHeap) Top() int {
	if len(mh.arr) == 1 {
		return -1
	}
	return mh.arr[1]
}

func (mh *MinHeap) Heapify(nums []int) {
	for _, n := range nums {
		mh.Push(n)
	}
}

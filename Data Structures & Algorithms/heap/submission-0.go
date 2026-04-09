type MinHeap struct {
	arr []int
}

func NewMinHeap() *MinHeap {
	return &MinHeap{
		arr: make([]int, 0),
	}
}

func (mh *MinHeap) Push(val int) {
	mh.arr = append(mh.arr, val)
	i := len(mh.arr) - 1

	for mh.arr[i] < mh.arr[i/2] {
		mh.arr[i/2], mh.arr[i] = mh.arr[i], mh.arr[i/2]
		i = i / 2
	}
}

func (mh *MinHeap) Pop() int {
	if len(mh.arr) == 0 {
		return -1
	}
	v := mh.arr[0]
	mh.arr = mh.arr[1:]
	return v
}

func (mh *MinHeap) Top() int {
	if len(mh.arr) == 0 {
		return -1
	}
	return mh.arr[0]
}

func (mh *MinHeap) Heapify(nums []int) {
	for _, n := range nums {
		mh.Push(n)
	}
}

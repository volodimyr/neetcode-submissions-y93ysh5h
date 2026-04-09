func merge(nums1 []int, m int, nums2 []int, n int) {
	for i := len(nums1) - 1; i >= m && m > 0; i-- {
		if nums1[m-1] > nums2[n-1] {
			nums1[i] = nums1[m-1]
			m--
		} else {
			nums1[i] = nums2[n-1]
			n--
		}
	}
	for i := n; i > 0; i-- {
		nums1[i-1] = nums2[n-1]
		n--
	}
}
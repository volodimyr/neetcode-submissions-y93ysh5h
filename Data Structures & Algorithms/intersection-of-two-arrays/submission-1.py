class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) == 0:
            return []
        if len(nums2) == 0:
            return []
        
        set2 = set(nums2)
        set1 = set(nums1)
        res = []

        for n in set1:
            if n in set2:
                res.append(n)
        return res
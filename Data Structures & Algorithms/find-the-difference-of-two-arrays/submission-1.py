class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        sn1=set(nums1)
        sn2=set(nums2)
        res1, res2 = [], []

        for key in sn1:
            if key not in sn2:
                res1.append(key)
        
        for key in sn2:
            if key not in sn1:
                res2.append(key)

        res = []
        res.append(res1)
        res.append(res2)
    
        return res

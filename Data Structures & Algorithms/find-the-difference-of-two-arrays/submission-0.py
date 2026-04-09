class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        countern1=Counter(nums1)
        countern2=Counter(nums2)
        res1, res2 = [], []

        for key in countern1:
            if key not in countern2:
                res1.append(key)
        
        for key in countern2:
            if key not in countern1:
                res2.append(key)
        res = []
        res.append(res1)
        res.append(res2)
    
        return res

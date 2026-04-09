class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = [0] * (len(nums1)+len(nums2))
        def merge():
            s = 0
            i = 0
            j = 0

            while i < len(nums1) and j < len(nums2):
                if nums1[i] <= nums2[j]:
                    arr[s] = nums1[i]
                    i+=1
                else:
                    arr[s] = nums2[j]
                    j+=1
                s+=1
            
            while i < len(nums1):
                arr[s] = nums1[i]
                i+=1
                s+=1
            
            while j < len(nums2):
                arr[s] = nums2[j]
                j+=1
                s+=1
        
        merge()

        if len(arr) % 2 == 1:
            return arr[len(arr)//2]
            
        return (arr[len(arr)//2] + arr[len(arr)//2-1]) / 2
        
            

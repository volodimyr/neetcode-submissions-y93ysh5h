class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        
        minv = -math.inf
        arr = []
        for n in preorder:
            while arr and arr[-1] < n:
                minv = arr.pop()

            if n <= minv:
                return False
            
            arr.append(n)
        
        return True
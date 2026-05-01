class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) == 1:
            return 1
        buckets = defaultdict(int)
        res = 0
        L = 0
        buckets[fruits[L]] = 1
        R = 1
        while True:
            if R == len(fruits):
                break
            buckets[fruits[R]] += 1
            while len(buckets) > 2:
                if buckets[fruits[L]] == 1:
                    del buckets[fruits[L]]
                else:
                    buckets[fruits[L]] -= 1
                L += 1
            
            res = max(res, R-L+1)
            R += 1
        return res

           


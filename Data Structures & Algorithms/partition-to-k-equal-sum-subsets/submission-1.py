class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        summ = sum(nums)
        if summ % k != 0:
            return False
        goal = summ // k
        N = len(nums)
        res = [0] * k
        nums.sort(reverse=True)

        def dfs(i):
            if i == N:
                return True
            for j in range(len(res)):
                if res[j] + nums[i] <= goal:
                    res[j] += nums[i]
                    if dfs(i+1):
                        return True
                    res[j] -= nums[i]
                if res[j] == 0:
                    break
            return False

        return dfs(0)
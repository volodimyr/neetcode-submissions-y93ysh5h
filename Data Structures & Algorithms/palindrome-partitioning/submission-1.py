class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def palindrome(L, R)->bool:
            while L < R:
                if s[L] != s[R]:
                    return False
                L+=1
                R-=1
            return True

        def backtrack(i: int, part: List[str]):
            if i >= len(s):
                res.append(part[:])
                return
            for j in range(i, len(s)):
                if palindrome(i, j):
                    part.append(s[i:j+1])
                    backtrack(j+1, part)
                    part.pop()

        res = []
        backtrack(0, [])
        return res
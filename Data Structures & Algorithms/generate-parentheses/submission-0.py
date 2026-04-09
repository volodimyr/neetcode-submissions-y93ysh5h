class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(op, cl, curStr):
            if len(curStr) == 2*n:
                subsets.append(curStr)
                return
            if op < n:
                backtrack(op+1, cl, curStr+'(')
            if cl < op:
                backtrack(op, cl+1, curStr+')')

        subsets = []
        backtrack(0, 0, "")
        return subsets
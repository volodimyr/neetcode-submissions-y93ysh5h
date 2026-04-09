numbers_map = {
    '2': "abc",
    '3': "def",
    '4': "ghi",
    '5': "jkl",
    '6': "mno",
    '7': "pqrs",
    '8': "tuv",
    '9': "wxyz",
}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        subsets = []

        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                subsets.append(curStr)
                return
            for char in numbers_map[digits[i]]:
                backtrack(i+1, curStr+char)
        backtrack(0, "")

        return subsets

# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         if not digits:
#             return []
#         subsets = [""]
#         for digit in digits:
#             tmp = []
#             for curStr in subsets:
#                 for c in numbers_map[digit]:
#                     tmp.append(curStr+c)
#             subsets = tmp
#         return subsets
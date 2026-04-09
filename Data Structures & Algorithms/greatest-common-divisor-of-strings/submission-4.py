class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ''
        if len(str1) < len(str2):
            str1, str2 = str2, str1

        prefix = len(str2)
        while prefix != 0:
            if len(str1) % prefix != 0 or len(str2) % prefix != 0:
                prefix-=1
                continue

            L,R = 0,prefix
            found = True
            while R <= len(str2):
                if str2[0:prefix] != str2[L:R]:
                    found = False
                    break
                L = R
                R = R+prefix
            
            if not found:
                prefix-=1
                continue

            L, R = 0, prefix
            while R <= len(str1):
                if str1[L:R] != str2[0:prefix]:
                    found = False
                    break
                L = R
                R = R+prefix

            if found:
                return str2[0:prefix]
            else:
                prefix-=1

        return ''
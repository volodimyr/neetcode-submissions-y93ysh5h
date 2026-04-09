class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 == str2:
            return str1
        if len(str1) < len(str2):
            str1, str2 = str2, str1

        p = []
        prefix = len(str2)
        while prefix != 0:
            if len(str1) % prefix != 0 or len(str2) % prefix != 0:
                prefix-=1
                continue

            L, R = 0, prefix
            L1, R1 = 0, prefix
            found = True
            p.append(prefix)
            while R <= len(str1):
                if str1[L:R] != str2[L1:R1]:
                    found = False
                    break
                L = R
                R = R+prefix
                if R1 + prefix > len(str2):
                    R1 = prefix
                    L1 = 0
                else:
                    L1 = R1
                    R1 = R1+prefix

            if found:
                return str2[0:prefix]
            else:
                prefix-=1

        return ''
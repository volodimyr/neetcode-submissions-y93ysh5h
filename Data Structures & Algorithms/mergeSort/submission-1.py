# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return divide(pairs,0,len(pairs)-1)

def divide(pairs, s, e):
    if e-s+1 <= 1:
        return pairs
    
    m = (s+e) // 2

    divide(pairs, s, m)
    divide(pairs, m+1, e)

    # merge part
    conquer(pairs, s, m, e)
    return pairs

def conquer(pairs, s, m, e):
    L = pairs[s:m+1]
    R = pairs[m+1:e+1]

    k = s
    i = 0
    j = 0

    while i < len(L) and j < len(R):
        if L[i].key <= R[j].key:
            pairs[k] = L[i]
            i+=1
        else:
            pairs[k] = R[j]
            j+=1
        k+=1
    
    while j < len(R):
        pairs[k] = R[j]
        j+=1
        k+=1

    while i < len(L):
        pairs[k] = L[i]
        i+=1
        k+=1
        
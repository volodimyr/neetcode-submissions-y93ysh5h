class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        w = 0
        list = []
        for char in blocks:
            if char == 'W':
                w+=1
            list.append(char)
            k-=1
            if k == 0:
                break
        if w == 0:
            return 0
        min_replace = w

        for i in range(k, len(blocks), 1):
            if blocks[i] == 'W':
                w+=1
            list.append(blocks[i])
            if list[0] == 'W':
                w-=1
            min_replace = min(min_replace, w)
            del list[0]
        
        return min_replace

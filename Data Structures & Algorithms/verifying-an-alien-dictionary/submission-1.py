class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {}
        for i in range(len(order)):
            order_map[order[i]] = i
        
        def sort_custom(word: str):
            arr = []
            for char in word:
                arr.append(order_map[char])
            return arr
        
        return words == sorted(words, key=sort_custom)
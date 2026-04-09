numbers = {
    '2': [
        'a','b','c'
        ],
    '3': [
        'd','e','f'
        ],
    '4':[
        'g','h','i'
        ],
    '5': [
        'j','k','l'
        ],
    '6': [
        'm','n','o'
        ],
    '7': [
        'p','q','r','s'
        ],
    '8': [
        't','u','v'
        ],
    '9': [
        'w','x','y','z'
        ],
    }

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        if len(digits) == 1:
            return numbers[digits]
        subsets = []
        for char0 in numbers[digits[0]]:
            if len(digits) > 1:
                for char1 in numbers[digits[1]]:
                    if len(digits) > 2:
                        for char2 in numbers[digits[2]]:
                            if len(digits)> 3:
                                for char3 in numbers[digits[3]]:
                                    if len(digits) >4:
                                        pass
                                    else:
                                        subsets.append(char0+char1+char2+char3)
                            else:
                                subsets.append(char0+char1+char2)
                    else:
                        subsets.append(char0+char1)
            else:
                subsets.append(char0)                

        
        return subsets
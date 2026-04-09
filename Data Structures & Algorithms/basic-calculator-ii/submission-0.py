class Solution:
    def calculate(self, s: str) -> int:
        arr = []
        i = 0
        while i < len(s):
            if s[i] == ' ':
                i += 1
                continue
            if is_operand(s[i]):
                arr.append(s[i])
                i += 1
            else:
                n = s[i]
                i += 1
                while i < len(s) and is_num(s[i]):
                    n += s[i]
                    i += 1
                if len(arr) > 1 and (arr[-1] == '*' or arr[-1] == '/'):
                    if arr.pop() == '*':
                        arr.append(arr.pop() * int(n))
                    else:
                        num = arr.pop()
                        if num < 0:
                            num = -num
                            num = num // int(n)
                            arr.append(-num)
                        else:
                            arr.append(num // int(n))
                elif len(arr) > 1 and (arr[-1] == '+' or arr[-1] == '-'):
                    if arr.pop() == "+":
                        arr.append(int(n))
                    else:
                        num = int(n)
                        arr.append(-num)
                else:
                    arr.append(int(n))

        return sum(arr)
            

def is_operand(val):
    return val == '+' or val == '-' or val == '/' or val == '*'

def is_num(val):
    try:
        num = int(val)
    except ValueError:
        return False
    return True

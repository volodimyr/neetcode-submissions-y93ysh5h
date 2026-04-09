class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_str = ""
        current_num = ""
        
        for char in s:
            if char == ']':
                num = int(stack.pop()) if stack[-1] else 0
                prev_str = stack.pop()
                repeated = current_str * num
                current_str = prev_str + repeated
            elif char == '[':
                stack.append(current_str)
                stack.append(current_num)
                current_num = ""
                current_str = ""
            elif char.isdigit():
                current_num += char
            else:
                current_str += char
        
        return current_str
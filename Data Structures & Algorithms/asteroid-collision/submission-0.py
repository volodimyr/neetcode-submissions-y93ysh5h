class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for a in asteroids:
            destroyed = 0
            while destroyed < len(stack) and stack[len(stack) - 1 - destroyed] > 0 and a < 0:
                top = stack[len(stack) - 1 - destroyed]
                
                if top == -a:
                    destroyed += 1
                    a = 0
                    break
                elif top > -a:
                    a = 0
                    break
                else:  # top < -a
                    destroyed += 1
            
            if destroyed > 0:
                stack = stack[:len(stack) - destroyed]
            
            if a != 0:
                stack.append(a)
        
        return stack
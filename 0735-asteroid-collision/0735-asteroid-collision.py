class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        print(stack)
        for i in asteroids:
            while stack and i < 0 and stack[-1] > 0:
                s = i + stack[-1]
                if s < 0: 
                    stack.pop()
                elif s > 0:
                    i = 0
                else:
                    stack.pop()
                    i = 0
            if i:
                stack.append(i)
        return stack
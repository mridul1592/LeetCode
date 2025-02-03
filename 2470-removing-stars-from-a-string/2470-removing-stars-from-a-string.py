class Solution:
    def removeStars(self, s: str) -> str:
        op = []
        for i in s:
            if i != '*':
                op.append(i)
            elif i == '*':
                op.pop()
        
        return ''.join(op)
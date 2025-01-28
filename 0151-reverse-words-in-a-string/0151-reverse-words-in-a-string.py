class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split(' ')
        words = [w for w in words if w != '']
        return ' '.join(words[::-1])
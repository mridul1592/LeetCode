class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l, r = 0, k-1
        vow = {'a', 'e', 'i', 'o', 'u'}
        count = sum(1 for i in s[:k] if i in vow)
        maxV = count
        for i in range(len(s)-k):
            if s[i] in vow:
                count -= 1
            if s[i+k] in vow:
                count += 1
            maxV = max(maxV, count)
        
        return maxV
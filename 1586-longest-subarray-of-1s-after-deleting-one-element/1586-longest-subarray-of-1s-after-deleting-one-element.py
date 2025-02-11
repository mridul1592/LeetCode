class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if 0 not in nums:
            return n - 1
        l = 0
        z = 0
        maxLen = 0

        for r in range(n):
            if nums[r] == 0:
                z += 1

            while z > 1:
                if nums[l] == 0:
                    z -= 1
                l += 1
            
            maxLen = max(maxLen, r - l + 1 - z)

        return maxLen
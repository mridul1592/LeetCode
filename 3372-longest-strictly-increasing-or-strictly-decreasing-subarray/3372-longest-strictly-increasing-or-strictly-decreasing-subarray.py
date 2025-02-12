class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        longestInc = 1
        inc = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                inc += 1
                longestInc = max(longestInc, inc)
            else:
                inc = 1
        
        longestDec = 1
        dec = 1
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                dec += 1
                longestDec = max(longestDec, dec)
            else:
                dec = 1

        return max(longestDec, longestInc)
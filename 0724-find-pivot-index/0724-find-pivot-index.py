class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = 0
        l = len(nums)
        for i in range(l):
            left_sum = sum(nums[:i])
            right_sum = sum(nums[i+1:l])
            if left_sum == right_sum:
                return i
        
        return -1
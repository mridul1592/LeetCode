class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)

        for i, ele in enumerate(nums):
            right_sum -= ele
            if left_sum == right_sum:
                return i
            left_sum += ele
        
        return -1
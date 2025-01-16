class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        lastNonZeroAt = 0
        zero_count = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastNonZeroAt] = nums[i]
                lastNonZeroAt += 1
            elif nums[i] == 0:
                zero_count += 1 

        for i in range(lastNonZeroAt, len(nums)):
            nums[i] = 0
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxSum = nums[0]
        sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                sum += nums[i]
                maxSum = max(maxSum, sum)
            else:
                sum = nums[i]

        return maxSum
